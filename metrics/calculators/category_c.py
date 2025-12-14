"""Category C Calculator: File Operations Metrics (D049-D073)."""

from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set

from .base import BaseCalculator
from .helpers import mean, safe_divide
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryCCalculator(BaseCalculator):
    """Calculator for Category C: File Operations metrics."""

    category = "C"

    # File extension categories
    PYTHON_EXTENSIONS = {".py", ".pyw", ".pyx", ".pxd"}
    JS_EXTENSIONS = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}
    MARKDOWN_EXTENSIONS = {".md", ".markdown", ".mdx"}
    CONFIG_EXTENSIONS = {
        ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf",
        ".env", ".properties",
    }
    TEST_PATTERNS = {"test_", "_test", "spec_", "_spec", ".test.", ".spec."}

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _get_extension(self, file_path: str) -> str:
        """Get file extension from path."""
        return Path(file_path).suffix.lower()

    def _is_test_file(self, file_path: str) -> bool:
        """Check if file is a test file."""
        name = Path(file_path).name.lower()
        return any(pattern in name for pattern in self.TEST_PATTERNS)

    def _get_all_files(self) -> Dict[str, int]:
        """Get combined file operation counts."""
        all_files: Dict[str, int] = defaultdict(int)
        for path, count in self.data.files_read.items():
            all_files[path] += count
        for path, count in self.data.files_edited.items():
            all_files[path] += count
        for path, count in self.data.files_written.items():
            all_files[path] += count
        return dict(all_files)

    # D049-D055: File Counts and Frequency

    def _calc_d049(self, definition: MetricDefinition) -> MetricValue:
        """D049: Unique files read."""
        return self.create_value("D049", len(self.data.files_read))

    def _calc_d050(self, definition: MetricDefinition) -> MetricValue:
        """D050: Unique files edited."""
        return self.create_value("D050", len(self.data.files_edited))

    def _calc_d051(self, definition: MetricDefinition) -> MetricValue:
        """D051: File read frequency distribution."""
        if not self.data.files_read:
            return self.create_value("D051", {})

        # Create histogram of read counts
        count_dist: Dict[str, int] = defaultdict(int)
        for count in self.data.files_read.values():
            bucket = f"{count}x" if count <= 10 else "10+x"
            count_dist[bucket] += 1

        return self.create_value("D051", dict(count_dist), breakdown=dict(count_dist))

    def _calc_d052(self, definition: MetricDefinition) -> MetricValue:
        """D052: File edit frequency distribution."""
        if not self.data.files_edited:
            return self.create_value("D052", {})

        count_dist: Dict[str, int] = defaultdict(int)
        for count in self.data.files_edited.values():
            bucket = f"{count}x" if count <= 10 else "10+x"
            count_dist[bucket] += 1

        return self.create_value("D052", dict(count_dist), breakdown=dict(count_dist))

    def _calc_d053(self, definition: MetricDefinition) -> MetricValue:
        """D053: Most read file."""
        if not self.data.files_read:
            return self.create_value("D053", "None")

        most_read = max(self.data.files_read.items(), key=lambda x: x[1])[0]
        # Return just filename for privacy
        return self.create_value("D053", Path(most_read).name)

    def _calc_d054(self, definition: MetricDefinition) -> MetricValue:
        """D054: Most edited file."""
        if not self.data.files_edited:
            return self.create_value("D054", "None")

        most_edited = max(self.data.files_edited.items(), key=lambda x: x[1])[0]
        return self.create_value("D054", Path(most_edited).name)

    def _calc_d055(self, definition: MetricDefinition) -> MetricValue:
        """D055: Read to write ratio."""
        read_count = sum(self.data.files_read.values())
        write_count = (
            sum(self.data.files_edited.values()) +
            sum(self.data.files_written.values())
        )
        ratio = safe_divide(read_count, write_count)
        return self.create_value("D055", round(ratio, 2))

    # D056-D063: File Types and Creation

    def _calc_d056(self, definition: MetricDefinition) -> MetricValue:
        """D056: New file creation rate per session."""
        write_count = len(self.data.files_written)
        rate = safe_divide(write_count, len(self.data.sessions))
        return self.create_value("D056", round(rate, 2))

    def _calc_d057(self, definition: MetricDefinition) -> MetricValue:
        """D057: File deletion rate per session."""
        # Estimate from Bash tool calls with rm/delete
        rm_count = sum(
            1 for tc in self.data.tool_calls
            if tc.tool_name == "Bash" and tc.file_path and "rm " in str(tc.file_path)
        )
        rate = safe_divide(rm_count, len(self.data.sessions))
        return self.create_value("D057", round(rate, 4))

    def _calc_d058(self, definition: MetricDefinition) -> MetricValue:
        """D058: File type distribution by extension."""
        all_files = self._get_all_files()
        ext_counts: Dict[str, int] = defaultdict(int)

        for path in all_files.keys():
            ext = self._get_extension(path) or "no_ext"
            ext_counts[ext] += 1

        return self.create_value("D058", dict(ext_counts), breakdown=dict(ext_counts))

    def _calc_d059(self, definition: MetricDefinition) -> MetricValue:
        """D059: Python file ratio."""
        all_files = self._get_all_files()
        if not all_files:
            return self.create_value("D059", 0.0)

        python_count = sum(
            1 for path in all_files.keys()
            if self._get_extension(path) in self.PYTHON_EXTENSIONS
        )
        ratio = safe_divide(python_count, len(all_files))
        return self.create_value("D059", round(ratio, 4))

    def _calc_d060(self, definition: MetricDefinition) -> MetricValue:
        """D060: JavaScript/TypeScript file ratio."""
        all_files = self._get_all_files()
        if not all_files:
            return self.create_value("D060", 0.0)

        js_count = sum(
            1 for path in all_files.keys()
            if self._get_extension(path) in self.JS_EXTENSIONS
        )
        ratio = safe_divide(js_count, len(all_files))
        return self.create_value("D060", round(ratio, 4))

    def _calc_d061(self, definition: MetricDefinition) -> MetricValue:
        """D061: Markdown file ratio."""
        all_files = self._get_all_files()
        if not all_files:
            return self.create_value("D061", 0.0)

        md_count = sum(
            1 for path in all_files.keys()
            if self._get_extension(path) in self.MARKDOWN_EXTENSIONS
        )
        ratio = safe_divide(md_count, len(all_files))
        return self.create_value("D061", round(ratio, 4))

    def _calc_d062(self, definition: MetricDefinition) -> MetricValue:
        """D062: Config file ratio."""
        all_files = self._get_all_files()
        if not all_files:
            return self.create_value("D062", 0.0)

        config_count = sum(
            1 for path in all_files.keys()
            if self._get_extension(path) in self.CONFIG_EXTENSIONS
        )
        ratio = safe_divide(config_count, len(all_files))
        return self.create_value("D062", round(ratio, 4))

    def _calc_d063(self, definition: MetricDefinition) -> MetricValue:
        """D063: Test file ratio."""
        all_files = self._get_all_files()
        if not all_files:
            return self.create_value("D063", 0.0)

        test_count = sum(
            1 for path in all_files.keys()
            if self._is_test_file(path)
        )
        ratio = safe_divide(test_count, len(all_files))
        return self.create_value("D063", round(ratio, 4))

    # D064-D069: File Size and Churn

    def _calc_d064(self, definition: MetricDefinition) -> MetricValue:
        """D064: Average file size read."""
        # This would need actual file size data; estimate as 0 for now
        return self.create_value("D064", 0.0)

    def _calc_d065(self, definition: MetricDefinition) -> MetricValue:
        """D065: File versions created."""
        # This would need file history data
        return self.create_value("D065", 0)

    def _calc_d066(self, definition: MetricDefinition) -> MetricValue:
        """D066: Average versions per file."""
        versions = self.get_dependency_safe("D065", 0)
        files = self.get_dependency_safe("D050", 1)
        if files == 0:
            files = 1
        avg = safe_divide(versions, files)
        return self.create_value("D066", round(avg, 2))

    def _calc_d067(self, definition: MetricDefinition) -> MetricValue:
        """D067: Maximum versions per file."""
        # This would need file history data
        return self.create_value("D067", 0)

    def _calc_d068(self, definition: MetricDefinition) -> MetricValue:
        """D068: File churn rate (edits per day)."""
        total_edits = sum(self.data.files_edited.values())
        rate = safe_divide(total_edits, self.data.window_days)
        return self.create_value("D068", round(rate, 2))

    def _calc_d069(self, definition: MetricDefinition) -> MetricValue:
        """D069: File stability index (inverse of churn)."""
        churn = self.get_dependency_safe("D068", 1)
        if churn == 0:
            churn = 0.001  # Avoid division by zero
        stability = 1.0 / churn
        return self.create_value("D069", round(stability, 4))

    # D070-D073: Directory and Relationships

    def _calc_d070(self, definition: MetricDefinition) -> MetricValue:
        """D070: Directory depth distribution."""
        all_files = self._get_all_files()
        depth_counts: Dict[int, int] = defaultdict(int)

        for path in all_files.keys():
            depth = len(Path(path).parts)
            depth_counts[depth] += 1

        distribution = {str(k): v for k, v in sorted(depth_counts.items())}
        return self.create_value("D070", distribution, breakdown=distribution)

    def _calc_d071(self, definition: MetricDefinition) -> MetricValue:
        """D071: Files modified together (per session)."""
        session_files: Dict[str, Set[str]] = defaultdict(set)

        for tc in self.data.tool_calls:
            if tc.file_path and tc.tool_name in ("Edit", "Write"):
                # Use basename for privacy
                session_files[tc.session_id].add(Path(tc.file_path).name)

        # Count co-occurrences
        co_mods: Dict[str, int] = defaultdict(int)
        for files in session_files.values():
            file_list = sorted(files)
            for i, f1 in enumerate(file_list):
                for f2 in file_list[i + 1:]:
                    pair = f"{f1}+{f2}"
                    co_mods[pair] += 1

        # Get top 10 pairs
        top_pairs = dict(
            sorted(co_mods.items(), key=lambda x: x[1], reverse=True)[:10]
        )
        return self.create_value("D071", top_pairs, breakdown=top_pairs)

    def _calc_d072(self, definition: MetricDefinition) -> MetricValue:
        """D072: File dependency graph."""
        # Build simple graph based on Read->Edit sequences
        dependencies: Dict[str, List[str]] = defaultdict(list)

        read_files: Dict[str, str] = {}  # session -> last read file
        for tc in sorted(self.data.tool_calls, key=lambda x: x.timestamp):
            if tc.tool_name == "Read" and tc.file_path:
                read_files[tc.session_id] = tc.file_path
            elif tc.tool_name == "Edit" and tc.file_path:
                if tc.session_id in read_files:
                    read_file = read_files[tc.session_id]
                    if read_file != tc.file_path:
                        dependencies[Path(read_file).name].append(
                            Path(tc.file_path).name
                        )

        # Simplify to counts
        graph = {
            k: len(set(v))
            for k, v in dependencies.items()
        }
        return self.create_value("D072", graph, breakdown=graph)

    def _calc_d073(self, definition: MetricDefinition) -> MetricValue:
        """D073: Cross-directory edits ratio."""
        if not self.data.sessions:
            return self.create_value("D073", 0.0)

        session_dirs: Dict[str, Set[str]] = defaultdict(set)
        for tc in self.data.tool_calls:
            if tc.file_path and tc.tool_name in ("Edit", "Write"):
                parent = str(Path(tc.file_path).parent)
                session_dirs[tc.session_id].add(parent)

        multi_dir_sessions = sum(
            1 for dirs in session_dirs.values()
            if len(dirs) > 1
        )
        ratio = safe_divide(multi_dir_sessions, len(self.data.sessions))
        return self.create_value("D073", round(ratio, 4))
