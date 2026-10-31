import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.core.config import Settings, get_settings

_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def require_api_key(
    api_key: Annotated[str | None, Security(_api_key_header)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> None:
    """Only the Weathera app (which knows APP_API_KEY) may call protected routes."""
    expected = settings.app_api_key
    if not expected or not api_key or not secrets.compare_digest(api_key, expected):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
