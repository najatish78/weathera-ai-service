from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    """Liveness check used by the hosting platform and for quick testing."""
    return {"status": "ok"}
