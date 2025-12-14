"""Category A Calculator: Time & Activity Metrics (D001-D028)."""

from collections import defaultdict
from datetime import date, datetime, timedelta
from typing import Dict, List

from .base import BaseCalculator
from .helpers import (
    mean,
    median,
    std_dev,
    safe_divide,
    calculate_streak,
    calculate_current_streak,
    count_in_period,
    dates_from_sessions,
    filter_by_date_range,
)
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryACalculator(BaseCalculator):
    """Calculator for Category A: Time & Activity metrics."""

    category = "A"

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    # D001-D010: Active Time Calculations

    def _calc_d001(self, definition: MetricDefinition) -> MetricValue:
        """D001: Daily active hours - Hours active today."""
        today = date.today()
        hours = sum(
            s.duration_ms / 3600000
            for s in self.data.sessions
            if s.start_time and s.start_time.date() == today
        )
        return self.create_value("D001", round(hours, 2), window_days=1)

    def _calc_d002(self, definition: MetricDefinition) -> MetricValue:
        """D002: Weekly active hours - Hours active this week."""
        week_ago = datetime.now() - timedelta(days=7)
        hours = sum(
            s.duration_ms / 3600000
            for s in self.data.sessions
            if s.start_time and s.start_time >= week_ago
        )
        return self.create_value("D002", round(hours, 2), window_days=7)

    def _calc_d003(self, definition: MetricDefinition) -> MetricValue:
        """D003: Monthly active hours - Hours active this month."""
        hours = sum(s.duration_ms / 3600000 for s in self.data.sessions)
        return self.create_value("D003", round(hours, 2))

    def _calc_d004(self, definition: MetricDefinition) -> MetricValue:
        """D004: Total thinking time."""
        # This would need message-level thinking data
        # For now, estimate from messages with thinking
        thinking_minutes = sum(
            m.thinking_length / 1000  # Rough estimate
            for m in self.data.messages
            if m.has_thinking
        )
        return self.create_value("D004", round(thinking_minutes, 2))

    def _calc_d005(self, definition: MetricDefinition) -> MetricValue:
        """D005: Average response time."""
        # Estimate from tool call durations as proxy
        durations = [
            tc.duration_ms
            for tc in self.data.tool_calls
            if tc.duration_ms is not None
        ]
        avg_ms = mean(durations) if durations else 0
        return self.create_value("D005", round(avg_ms / 1000, 2))  # Convert to seconds

    def _calc_d006(self, definition: MetricDefinition) -> MetricValue:
        """D006: Longest session duration."""
        if not self.data.sessions:
            return self.create_value("D006", 0.0)
        max_duration = max(s.duration_ms for s in self.data.sessions)
        return self.create_value("D006", round(max_duration / 3600000, 2))

    def _calc_d007(self, definition: MetricDefinition) -> MetricValue:
        """D007: Average session duration."""
        if not self.data.sessions:
            return self.create_value("D007", 0.0)
        durations = [s.duration_ms for s in self.data.sessions]
        avg_hours = mean(durations) / 3600000
        return self.create_value("D007", round(avg_hours, 2))

    def _calc_d008(self, definition: MetricDefinition) -> MetricValue:
        """D008: Median session duration."""
        if not self.data.sessions:
            return self.create_value("D008", 0.0)
        durations = [s.duration_ms for s in self.data.sessions]
        med_hours = median(durations) / 3600000
        return self.create_value("D008", round(med_hours, 2))

    def _calc_d009(self, definition: MetricDefinition) -> MetricValue:
        """D009: Total API time (from tool executions)."""
        total_ms = sum(
            tc.duration_ms
            for tc in self.data.tool_calls
            if tc.duration_ms is not None
        )
        return self.create_value("D009", round(total_ms / 60000, 2))  # minutes

    def _calc_d010(self, definition: MetricDefinition) -> MetricValue:
        """D010: Average tool execution time."""
        durations = [
            tc.duration_ms
            for tc in self.data.tool_calls
            if tc.duration_ms is not None
        ]
        avg_ms = mean(durations) if durations else 0
        return self.create_value("D010", round(avg_ms, 2))

    # D011-D020: Time Distribution Analysis

    def _calc_d011(self, definition: MetricDefinition) -> MetricValue:
        """D011: Peak activity hour."""
        if not self.data.hourly_distribution:
            return self.create_value("D011", 0)
        peak_hour = max(
            self.data.hourly_distribution.items(),
            key=lambda x: x[1],
            default=(0, 0),
        )[0]
        return self.create_value("D011", peak_hour)

    def _calc_d012(self, definition: MetricDefinition) -> MetricValue:
        """D012: Peak productivity day (weekday with most activity)."""
        weekday_counts: Dict[int, int] = defaultdict(int)
        for session in self.data.sessions:
            if session.start_time:
                weekday_counts[session.start_time.weekday()] += 1

        if not weekday_counts:
            return self.create_value("D012", 0)

        peak_day = max(weekday_counts.items(), key=lambda x: x[1])[0]
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return self.create_value(
            "D012",
            day_names[peak_day],
            breakdown=dict(weekday_counts),
        )

    def _calc_d013(self, definition: MetricDefinition) -> MetricValue:
        """D013: Morning activity ratio (6AM-12PM)."""
        morning = count_in_period(self.data.hourly_distribution, 6, 12)
        total = sum(self.data.hourly_distribution.values())
        ratio = safe_divide(morning, total)
        return self.create_value("D013", round(ratio, 4))

    def _calc_d014(self, definition: MetricDefinition) -> MetricValue:
        """D014: Afternoon activity ratio (12PM-6PM)."""
        afternoon = count_in_period(self.data.hourly_distribution, 12, 18)
        total = sum(self.data.hourly_distribution.values())
        ratio = safe_divide(afternoon, total)
        return self.create_value("D014", round(ratio, 4))

    def _calc_d015(self, definition: MetricDefinition) -> MetricValue:
        """D015: Evening activity ratio (6PM-12AM)."""
        evening = count_in_period(self.data.hourly_distribution, 18, 24)
        total = sum(self.data.hourly_distribution.values())
        ratio = safe_divide(evening, total)
        return self.create_value("D015", round(ratio, 4))

    def _calc_d016(self, definition: MetricDefinition) -> MetricValue:
        """D016: Night activity ratio (12AM-6AM)."""
        night = count_in_period(self.data.hourly_distribution, 0, 6)
        total = sum(self.data.hourly_distribution.values())
        ratio = safe_divide(night, total)
        return self.create_value("D016", round(ratio, 4))

    def _calc_d017(self, definition: MetricDefinition) -> MetricValue:
        """D017: Weekday vs weekend ratio."""
        weekday_count = 0
        weekend_count = 0
        for session in self.data.sessions:
            if session.start_time:
                if session.start_time.weekday() < 5:
                    weekday_count += 1
                else:
                    weekend_count += 1
        ratio = safe_divide(weekday_count, weekend_count, default=float("inf"))
        return self.create_value("D017", round(ratio, 2) if ratio != float("inf") else 0)

    def _calc_d018(self, definition: MetricDefinition) -> MetricValue:
        """D018: Session start time variance."""
        hours = [
            s.start_time.hour + s.start_time.minute / 60
            for s in self.data.sessions
            if s.start_time
        ]
        variance = std_dev(hours) if hours else 0
        return self.create_value("D018", round(variance, 2))

    def _calc_d019(self, definition: MetricDefinition) -> MetricValue:
        """D019: Session start time distribution."""
        distribution = dict(self.data.hourly_distribution)
        return self.create_value("D019", distribution, breakdown=distribution)

    def _calc_d020(self, definition: MetricDefinition) -> MetricValue:
        """D020: Session end time distribution."""
        end_dist: Dict[int, int] = defaultdict(int)
        for session in self.data.sessions:
            if session.end_time:
                end_dist[session.end_time.hour] += 1
        distribution = dict(end_dist)
        return self.create_value("D020", distribution, breakdown=distribution)

    # D021-D028: Streaks and Frequency

    def _calc_d021(self, definition: MetricDefinition) -> MetricValue:
        """D021: Longest activity streak."""
        dates = dates_from_sessions(self.data.sessions)
        streak = calculate_streak(dates)
        return self.create_value("D021", streak)

    def _calc_d022(self, definition: MetricDefinition) -> MetricValue:
        """D022: Current activity streak."""
        dates = dates_from_sessions(self.data.sessions)
        streak = calculate_current_streak(dates)
        return self.create_value("D022", streak)

    def _calc_d023(self, definition: MetricDefinition) -> MetricValue:
        """D023: Weekly active days."""
        week_ago = datetime.now() - timedelta(days=7)
        active_dates = set()
        for session in self.data.sessions:
            if session.start_time and session.start_time >= week_ago:
                active_dates.add(session.start_time.date())
        return self.create_value("D023", len(active_dates), window_days=7)

    def _calc_d024(self, definition: MetricDefinition) -> MetricValue:
        """D024: Monthly active days."""
        active_dates = set(
            s.start_time.date()
            for s in self.data.sessions
            if s.start_time
        )
        return self.create_value("D024", len(active_dates))

    def _calc_d025(self, definition: MetricDefinition) -> MetricValue:
        """D025: Average sessions per active day."""
        active_days = self.get_dependency_safe("D024", 1)
        if active_days == 0:
            active_days = 1
        avg = safe_divide(len(self.data.sessions), active_days)
        return self.create_value("D025", round(avg, 2))

    def _calc_d026(self, definition: MetricDefinition) -> MetricValue:
        """D026: Session frequency (sessions per calendar day)."""
        rate = safe_divide(len(self.data.sessions), self.data.window_days)
        return self.create_value("D026", round(rate, 2))

    def _calc_d027(self, definition: MetricDefinition) -> MetricValue:
        """D027: Inter-session gap (average time between sessions)."""
        if len(self.data.sessions) < 2:
            return self.create_value("D027", 0.0)

        sorted_sessions = sorted(
            self.data.sessions,
            key=lambda s: s.start_time if s.start_time else datetime.min,
        )

        gaps = []
        for i in range(1, len(sorted_sessions)):
            if sorted_sessions[i].start_time and sorted_sessions[i - 1].end_time:
                gap = (
                    sorted_sessions[i].start_time - sorted_sessions[i - 1].end_time
                ).total_seconds() / 3600
                if gap > 0:
                    gaps.append(gap)

        avg_gap = mean(gaps) if gaps else 0
        return self.create_value("D027", round(avg_gap, 2))

    def _calc_d028(self, definition: MetricDefinition) -> MetricValue:
        """D028: Activity density (messages per active hour)."""
        total_hours = self.get_dependency_safe("D003", 1)
        if total_hours == 0:
            total_hours = 1
        density = safe_divide(self.data.total_messages, total_hours)
        return self.create_value("D028", round(density, 2))
