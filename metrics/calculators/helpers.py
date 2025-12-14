"""Statistical calculation helpers for metric calculators."""

import math
from datetime import date, datetime, timedelta
from typing import Dict, List, Optional, Sequence, Tuple, Union


def safe_divide(
    numerator: Union[int, float],
    denominator: Union[int, float],
    default: float = 0.0,
) -> float:
    """Safely divide two numbers, returning default if denominator is zero.

    Args:
        numerator: The numerator
        denominator: The denominator
        default: Value to return if denominator is zero

    Returns:
        Result of division or default
    """
    if denominator == 0:
        return default
    return numerator / denominator


def mean(values: Sequence[Union[int, float]]) -> float:
    """Calculate arithmetic mean of values.

    Args:
        values: Sequence of numbers

    Returns:
        Mean value, or 0.0 if empty
    """
    if not values:
        return 0.0
    return sum(values) / len(values)


def median(values: Sequence[Union[int, float]]) -> float:
    """Calculate median of values.

    Args:
        values: Sequence of numbers

    Returns:
        Median value, or 0.0 if empty
    """
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def percentile(
    values: Sequence[Union[int, float]], p: float
) -> float:
    """Calculate percentile of values.

    Args:
        values: Sequence of numbers
        p: Percentile (0-100)

    Returns:
        Value at percentile, or 0.0 if empty
    """
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    idx = (n - 1) * (p / 100)
    lower = int(idx)
    upper = lower + 1
    if upper >= n:
        return sorted_vals[-1]
    weight = idx - lower
    return sorted_vals[lower] * (1 - weight) + sorted_vals[upper] * weight


def variance(values: Sequence[Union[int, float]]) -> float:
    """Calculate population variance of values.

    Args:
        values: Sequence of numbers

    Returns:
        Variance, or 0.0 if less than 2 values
    """
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def std_dev(values: Sequence[Union[int, float]]) -> float:
    """Calculate population standard deviation.

    Args:
        values: Sequence of numbers

    Returns:
        Standard deviation, or 0.0 if less than 2 values
    """
    return math.sqrt(variance(values))


def linear_regression_slope(
    values: List[Tuple[float, float]]
) -> float:
    """Calculate slope of linear regression line.

    Args:
        values: List of (x, y) coordinate pairs

    Returns:
        Slope of best-fit line, or 0.0 if insufficient data
    """
    if len(values) < 2:
        return 0.0

    n = len(values)
    sum_x = sum(x for x, _ in values)
    sum_y = sum(y for _, y in values)
    sum_xy = sum(x * y for x, y in values)
    sum_x2 = sum(x * x for x, _ in values)

    denominator = n * sum_x2 - sum_x ** 2
    if denominator == 0:
        return 0.0
    return (n * sum_xy - sum_x * sum_y) / denominator


def calculate_streak(
    dates: List[date], end_date: Optional[date] = None
) -> int:
    """Calculate longest consecutive day streak.

    Args:
        dates: List of dates with activity
        end_date: Optional end date (default: today)

    Returns:
        Length of longest streak
    """
    if not dates:
        return 0

    sorted_dates = sorted(set(dates))
    max_streak = 1
    current = 1

    for i in range(1, len(sorted_dates)):
        if (sorted_dates[i] - sorted_dates[i - 1]).days == 1:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 1

    return max_streak


def calculate_current_streak(
    dates: List[date], end_date: Optional[date] = None
) -> int:
    """Calculate current consecutive day streak ending at end_date.

    Args:
        dates: List of dates with activity
        end_date: Date to end the streak at (default: today)

    Returns:
        Current streak length (0 if no activity on end_date)
    """
    if not dates:
        return 0

    if end_date is None:
        end_date = date.today()

    sorted_dates = sorted(set(dates), reverse=True)

    # Check if there's activity on end_date
    if sorted_dates[0] != end_date:
        return 0

    streak = 1
    for i in range(1, len(sorted_dates)):
        if (sorted_dates[i - 1] - sorted_dates[i]).days == 1:
            streak += 1
        else:
            break

    return streak


def shannon_entropy(distribution: Dict[str, int]) -> float:
    """Calculate Shannon entropy (diversity index).

    Higher values indicate more diverse/even distribution.

    Args:
        distribution: Dictionary mapping categories to counts

    Returns:
        Shannon entropy in bits, or 0.0 if empty
    """
    total = sum(distribution.values())
    if total == 0:
        return 0.0

    entropy = 0.0
    for count in distribution.values():
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)

    return entropy


def normalize(
    value: Union[int, float],
    min_val: Union[int, float],
    max_val: Union[int, float],
) -> float:
    """Normalize a value to 0-1 range.

    Args:
        value: Value to normalize
        min_val: Minimum of range
        max_val: Maximum of range

    Returns:
        Normalized value (0-1), clamped to range
    """
    if max_val == min_val:
        return 0.5
    normalized = (value - min_val) / (max_val - min_val)
    return max(0.0, min(1.0, normalized))


def get_time_of_day_period(hour: int) -> str:
    """Get time-of-day period for an hour.

    Args:
        hour: Hour (0-23)

    Returns:
        Period name: "night", "morning", "afternoon", "evening"
    """
    if 0 <= hour < 6:
        return "night"
    elif 6 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    else:
        return "evening"


def count_in_period(
    hourly_distribution: Dict[int, int], start_hour: int, end_hour: int
) -> int:
    """Count total in hourly distribution for a period.

    Args:
        hourly_distribution: Hour -> count mapping
        start_hour: Start hour (inclusive)
        end_hour: End hour (exclusive)

    Returns:
        Total count in period
    """
    return sum(
        count
        for hour, count in hourly_distribution.items()
        if start_hour <= hour < end_hour
    )


def dates_from_sessions(sessions: list) -> List[date]:
    """Extract unique dates from sessions.

    Args:
        sessions: List of SessionData objects

    Returns:
        List of unique dates
    """
    dates = set()
    for session in sessions:
        if session.start_time:
            dates.add(session.start_time.date())
    return list(dates)


def filter_by_date_range(
    sessions: list,
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
) -> list:
    """Filter sessions by date range.

    Args:
        sessions: List of SessionData objects
        start: Start datetime (inclusive)
        end: End datetime (inclusive)

    Returns:
        Filtered list of sessions
    """
    result = []
    for session in sessions:
        if session.start_time is None:
            continue
        if start and session.start_time < start:
            continue
        if end and session.start_time > end:
            continue
        result.append(session)
    return result
