"""FastAPI entry point; only health is implemented in Phase 0."""

from fastapi import FastAPI

from concierge.config import settings

app = FastAPI(title=settings.app_name, version="0.1.0", description="Phase 0 foundation")


@app.get("/health", tags=["operations"])
def health() -> dict[str, str]:
    """Return process health without touching external services."""
    return {"status": "ok", "phase": "foundation"}
