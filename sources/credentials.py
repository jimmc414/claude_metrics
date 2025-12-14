"""Credentials source extractor."""

from typing import Any, Dict

from utils import get_claude_dir, read_json_file
from .base import BaseSource


class CredentialsSource(BaseSource):
    """Extractor for ~/.claude/.credentials.json.

    Contains OAuth authentication tokens and subscription info.
    This source contains highly sensitive data and is redacted by default.
    """

    name = "credentials"
    description = "OAuth tokens and subscription information"
    source_paths = ["~/.claude/.credentials.json"]

    def extract(self) -> Dict[str, Any]:
        """Extract credentials data.

        Note: Sensitive fields are redacted by default.
        Use include_sensitive=True to include actual values.

        Returns:
            Dictionary containing:
            - claudeAiOauth: OAuth tokens and subscription info
              - accessToken: OAuth access token (redacted by default)
              - refreshToken: OAuth refresh token (redacted by default)
              - expiresAt: Token expiration timestamp
              - scopes: Granted OAuth scopes
              - subscriptionType: "max" | "pro" | "free"
              - rateLimitTier: Rate limit tier name
        """
        path = get_claude_dir() / ".credentials.json"
        data = read_json_file(path)

        if data is None:
            return {"error": "Credentials file not found", "path": str(path)}

        result = {
            "path": str(path),
            "exists": True,
        }

        oauth = data.get("claudeAiOauth", {})

        # Extract non-sensitive fields
        result["subscription_type"] = oauth.get("subscriptionType")
        result["rate_limit_tier"] = oauth.get("rateLimitTier")
        result["scopes"] = oauth.get("scopes", [])
        result["expires_at"] = oauth.get("expiresAt")

        # Include sensitive fields only if requested
        if self.include_sensitive:
            result["access_token"] = oauth.get("accessToken")
            result["refresh_token"] = oauth.get("refreshToken")
        else:
            result["access_token"] = "[REDACTED]"
            result["refresh_token"] = "[REDACTED]"

        # Check if tokens are present (without revealing them)
        result["has_access_token"] = bool(oauth.get("accessToken"))
        result["has_refresh_token"] = bool(oauth.get("refreshToken"))

        return result

    def get_summary(self) -> Dict[str, Any]:
        """Get credentials summary."""
        data = self.get_data()

        if "error" in data:
            return {"source": self.name, "error": data["error"]}

        return {
            "source": self.name,
            "exists": data.get("exists", False),
            "subscription_type": data.get("subscription_type"),
            "rate_limit_tier": data.get("rate_limit_tier"),
            "scopes": data.get("scopes", []),
            "has_valid_tokens": (
                data.get("has_access_token", False)
                and data.get("has_refresh_token", False)
            ),
        }
