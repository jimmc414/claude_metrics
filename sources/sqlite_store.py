"""SQLite store extractor."""

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_claude_dir, format_bytes


class SqliteStoreSource(BaseSource):
    """Extract data from Claude Code's SQLite message store."""

    name = "sqlite_store"
    description = "SQLite message database"
    source_paths = ["~/.claude/__store.db"]

    def _get_store_path(self) -> Path:
        """Get the SQLite store path."""
        return get_claude_dir() / "__store.db"

    def _get_table_info(self, cursor: sqlite3.Cursor) -> Dict[str, Dict[str, Any]]:
        """Get information about all tables in the database."""
        tables = {}

        # Get list of tables
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        )

        for (table_name,) in cursor.fetchall():
            # Get row count
            try:
                cursor.execute(f"SELECT COUNT(*) FROM [{table_name}]")
                row_count = cursor.fetchone()[0]
            except sqlite3.Error:
                row_count = 0

            # Get column info
            cursor.execute(f"PRAGMA table_info([{table_name}])")
            columns = [
                {"name": row[1], "type": row[2], "notnull": bool(row[3]), "pk": bool(row[5])}
                for row in cursor.fetchall()
            ]

            tables[table_name] = {
                "row_count": row_count,
                "columns": columns,
            }

        return tables

    def _get_assistant_message_stats(self, cursor: sqlite3.Cursor) -> Dict[str, Any]:
        """Get statistics from assistant_messages table."""
        stats = {
            "total_messages": 0,
            "total_cost_usd": 0.0,
            "models_used": [],
            "sessions_count": 0,
            "date_range": {"first": None, "last": None},
        }

        try:
            # Total messages and cost
            cursor.execute("""
                SELECT
                    COUNT(*) as total,
                    COALESCE(SUM(cost_usd), 0) as total_cost,
                    COUNT(DISTINCT session_id) as sessions,
                    MIN(timestamp) as first_ts,
                    MAX(timestamp) as last_ts
                FROM assistant_messages
            """)
            row = cursor.fetchone()
            if row:
                stats["total_messages"] = row[0]
                stats["total_cost_usd"] = round(row[1], 4) if row[1] else 0.0
                stats["sessions_count"] = row[2]

                # Convert timestamps
                if row[3]:
                    try:
                        stats["date_range"]["first"] = datetime.fromtimestamp(
                            row[3] / 1000
                        ).isoformat()
                    except (ValueError, OSError):
                        pass
                if row[4]:
                    try:
                        stats["date_range"]["last"] = datetime.fromtimestamp(
                            row[4] / 1000
                        ).isoformat()
                    except (ValueError, OSError):
                        pass

            # Models used
            cursor.execute("""
                SELECT DISTINCT model FROM assistant_messages
                WHERE model IS NOT NULL AND model != ''
            """)
            stats["models_used"] = sorted([row[0] for row in cursor.fetchall()])

        except sqlite3.Error:
            pass

        return stats

    def _get_model_usage(self, cursor: sqlite3.Cursor) -> List[Dict[str, Any]]:
        """Get per-model usage statistics."""
        usage = []

        try:
            cursor.execute("""
                SELECT
                    model,
                    COUNT(*) as message_count,
                    COALESCE(SUM(cost_usd), 0) as total_cost
                FROM assistant_messages
                WHERE model IS NOT NULL AND model != ''
                GROUP BY model
                ORDER BY total_cost DESC
            """)

            for row in cursor.fetchall():
                usage.append({
                    "model": row[0],
                    "message_count": row[1],
                    "total_cost_usd": round(row[2], 4) if row[2] else 0.0,
                })

        except sqlite3.Error:
            pass

        return usage

    def extract(self) -> Dict[str, Any]:
        """Extract data from SQLite store."""
        store_path = self._get_store_path()

        if not store_path.exists():
            return {
                "database_exists": False,
                "path": str(store_path),
                "tables": {},
                "assistant_stats": {},
                "model_usage": [],
            }

        try:
            size = store_path.stat().st_size
        except (OSError, PermissionError):
            size = 0

        result = {
            "database_exists": True,
            "path": str(store_path),
            "size_bytes": size,
            "size_human": format_bytes(size),
            "tables": {},
            "assistant_stats": {},
            "model_usage": [],
        }

        try:
            # Open database in read-only mode
            conn = sqlite3.connect(f"file:{store_path}?mode=ro", uri=True)
            cursor = conn.cursor()

            # Get table information
            result["tables"] = self._get_table_info(cursor)

            # Get assistant message statistics
            if "assistant_messages" in result["tables"]:
                result["assistant_stats"] = self._get_assistant_message_stats(cursor)
                result["model_usage"] = self._get_model_usage(cursor)

            conn.close()

        except sqlite3.Error as e:
            result["error"] = str(e)

        return result

    def to_sqlite(self, db) -> None:
        """Write SQLite store summary to database."""
        data = self.get_data()
        if data.get("database_exists"):
            db.insert_sqlite_store_summary(data)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of SQLite store."""
        data = self.get_data()

        if not data.get("database_exists"):
            return {
                "source": self.name,
                "database_exists": False,
            }

        assistant_stats = data.get("assistant_stats", {})

        return {
            "source": self.name,
            "database_exists": True,
            "size_bytes": data.get("size_bytes", 0),
            "table_count": len(data.get("tables", {})),
            "total_messages": assistant_stats.get("total_messages", 0),
            "total_cost_usd": assistant_stats.get("total_cost_usd", 0.0),
            "models_used": len(assistant_stats.get("models_used", [])),
        }
