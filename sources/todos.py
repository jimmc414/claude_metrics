"""Todos source extractor."""

from collections import defaultdict
from typing import Any, Dict, List

from database import MetricsDatabase
from utils import get_claude_dir, read_json_file, iter_json_files
from .base import BaseSource


class TodosSource(BaseSource):
    """Extractor for ~/.claude/todos/*.json.

    Contains task/todo lists per session with status tracking.
    """

    name = "todos"
    description = "Task/todo lists per session"
    source_paths = ["~/.claude/todos/*.json"]

    def extract(self) -> Dict[str, Any]:
        """Extract todo data.

        Returns:
            Dictionary containing:
            - total_files: Number of todo files
            - total_todos: Total todo items across all files
            - by_status: Counts by status
            - todos: List of all todos with session info
        """
        todos_dir = get_claude_dir() / "todos"

        if not todos_dir.exists():
            return {"error": "Todos directory not found", "path": str(todos_dir)}

        all_todos = []
        by_status = defaultdict(int)
        by_session = {}
        file_count = 0

        for todo_file in iter_json_files(todos_dir):
            file_count += 1
            session_id = todo_file.stem

            todos = read_json_file(todo_file)
            if not todos or not isinstance(todos, list):
                continue

            session_todos = []
            for todo in todos:
                if not isinstance(todo, dict):
                    continue

                status = todo.get("status", "unknown")
                by_status[status] += 1

                todo_entry = {
                    "id": todo.get("id"),
                    "session_id": session_id,
                    "content": todo.get("content", ""),
                    "status": status,
                    "priority": todo.get("priority"),
                    "active_form": todo.get("activeForm"),
                }
                all_todos.append(todo_entry)
                session_todos.append(todo_entry)

            by_session[session_id] = {
                "count": len(session_todos),
                "completed": sum(1 for t in session_todos if t["status"] == "completed"),
                "pending": sum(1 for t in session_todos if t["status"] == "pending"),
                "in_progress": sum(1 for t in session_todos if t["status"] == "in_progress"),
            }

        return {
            "path": str(todos_dir),
            "total_files": file_count,
            "total_todos": len(all_todos),
            "by_status": dict(by_status),
            "session_count": len(by_session),
            "todos": all_todos,
            "by_session": by_session,
        }

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write todos to SQLite."""
        data = self.get_data()

        if "error" in data or db.conn is None:
            return

        todos = data.get("todos", [])

        for todo in todos:
            db.conn.execute(
                """
                INSERT OR REPLACE INTO todos
                (id, session_id, content, status, priority, active_form)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    todo.get("id"),
                    todo.get("session_id"),
                    todo.get("content"),
                    todo.get("status"),
                    todo.get("priority"),
                    todo.get("active_form"),
                ),
            )

        db.commit()

    def get_summary(self) -> Dict[str, Any]:
        """Get todos summary."""
        data = self.get_data()

        if "error" in data:
            return {"source": self.name, "error": data["error"]}

        by_status = data.get("by_status", {})
        total = data.get("total_todos", 0)

        completion_rate = 0
        if total > 0:
            completed = by_status.get("completed", 0)
            completion_rate = round(completed / total * 100, 1)

        return {
            "source": self.name,
            "total_files": data.get("total_files", 0),
            "total_todos": total,
            "by_status": by_status,
            "session_count": data.get("session_count", 0),
            "completion_rate_pct": completion_rate,
        }
