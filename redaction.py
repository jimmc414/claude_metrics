"""Sensitive data redaction for Claude Metrics."""

import hashlib
import re
from typing import Any, Dict, List, Set


# Fields that should be completely redacted
REDACT_FIELDS: Set[str] = {
    # OAuth tokens
    "accessToken",
    "access_token",
    "refreshToken",
    "refresh_token",
    "token",
    "bearer",

    # API keys
    "apiKey",
    "api_key",
    "apikey",
    "secret",
    "secretKey",
    "secret_key",

    # Passwords
    "password",
    "passwd",
}

# Fields that should be hashed (preserving uniqueness but obscuring value)
HASH_FIELDS: Set[str] = {
    "userID",
    "user_id",
    "userId",
}

# Patterns to redact in string values
REDACT_PATTERNS: List[tuple] = [
    # Bearer tokens
    (re.compile(r'Bearer\s+[A-Za-z0-9\-_]+\.?[A-Za-z0-9\-_]*\.?[A-Za-z0-9\-_]*', re.I), "[BEARER_REDACTED]"),
    # API keys (common formats)
    (re.compile(r'sk-[A-Za-z0-9]{32,}', re.I), "[API_KEY_REDACTED]"),
    (re.compile(r'api[_-]?key["\s:=]+["\']?[A-Za-z0-9\-_]{20,}', re.I), "[API_KEY_REDACTED]"),
]


def hash_value(value: str) -> str:
    """Hash a value for privacy while preserving uniqueness."""
    return hashlib.sha256(value.encode()).hexdigest()[:16]


def redact_value(key: str, value: Any, include_sensitive: bool = False) -> Any:
    """Redact a single value based on its key.

    Args:
        key: The field name/key
        value: The value to potentially redact
        include_sensitive: If True, return value unchanged

    Returns:
        The original value, redacted string, or hashed string
    """
    if include_sensitive:
        return value

    key_lower = key.lower()

    # Check if this field should be completely redacted
    if key in REDACT_FIELDS or key_lower in {f.lower() for f in REDACT_FIELDS}:
        return "[REDACTED]"

    # Check if this field should be hashed
    if key in HASH_FIELDS or key_lower in {f.lower() for f in HASH_FIELDS}:
        if isinstance(value, str):
            return f"[HASHED:{hash_value(value)}]"
        return "[HASHED]"

    return value


def redact_string(value: str, include_sensitive: bool = False) -> str:
    """Redact sensitive patterns in a string value.

    Args:
        value: The string to check for sensitive patterns
        include_sensitive: If True, return value unchanged

    Returns:
        The string with sensitive patterns redacted
    """
    if include_sensitive or not isinstance(value, str):
        return value

    result = value
    for pattern, replacement in REDACT_PATTERNS:
        result = pattern.sub(replacement, result)

    return result


def redact_dict(data: Dict[str, Any], include_sensitive: bool = False) -> Dict[str, Any]:
    """Recursively redact sensitive fields in a dictionary.

    Args:
        data: The dictionary to redact
        include_sensitive: If True, return data unchanged

    Returns:
        A new dictionary with sensitive fields redacted
    """
    if include_sensitive:
        return data

    if not isinstance(data, dict):
        return data

    result = {}
    for key, value in data.items():
        # First check if this key should be redacted
        redacted_value = redact_value(key, value, include_sensitive)

        if redacted_value != value:
            # Value was redacted
            result[key] = redacted_value
        elif isinstance(value, dict):
            # Recurse into nested dicts
            result[key] = redact_dict(value, include_sensitive)
        elif isinstance(value, list):
            # Handle lists
            result[key] = redact_list(value, include_sensitive)
        elif isinstance(value, str):
            # Check for patterns in string values
            result[key] = redact_string(value, include_sensitive)
        else:
            result[key] = value

    return result


def redact_list(data: List[Any], include_sensitive: bool = False) -> List[Any]:
    """Recursively redact sensitive fields in a list.

    Args:
        data: The list to redact
        include_sensitive: If True, return data unchanged

    Returns:
        A new list with sensitive fields redacted
    """
    if include_sensitive:
        return data

    result = []
    for item in data:
        if isinstance(item, dict):
            result.append(redact_dict(item, include_sensitive))
        elif isinstance(item, list):
            result.append(redact_list(item, include_sensitive))
        elif isinstance(item, str):
            result.append(redact_string(item, include_sensitive))
        else:
            result.append(item)

    return result
