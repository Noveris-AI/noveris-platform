import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text

from navima_shared.db.session import engine

ENABLE_API_DOCS = os.getenv("ENABLE_API_DOCS", "true").lower() == "true"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await engine.dispose()


app = FastAPI(
    title="Navima API",
    version="0.1.0",
    docs_url="/docs" if ENABLE_API_DOCS else None,
    redoc_url="/redoc" if ENABLE_API_DOCS else None,
    openapi_url="/openapi.json" if ENABLE_API_DOCS else None,
    lifespan=lifespan,
)


@app.get("/health/live", tags=["health"])
async def health_live() -> JSONResponse:
    return JSONResponse(content={"status": "ok"})


@app.get("/health/ready", tags=["health"])
async def health_ready() -> JSONResponse:
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return JSONResponse(content={"status": "ok"})
    except Exception:
        return JSONResponse(
            status_code=503,
            content={"status": "not_ready", "detail": "database_unavailable"},
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
