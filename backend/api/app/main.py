from fastapi import FastAPI
from fastapi.responses import JSONResponse
from navima_shared.db.session import engine
from sqlalchemy import text

from app.core.config import settings
from app.core.cors import add_cors_middleware
from app.core.errors import NavimaError, navima_exception_handler
from app.core.events import lifespan

app = FastAPI(
    title="Navima API",
    version="0.1.0",
    docs_url="/docs" if settings.enable_api_docs else None,
    redoc_url="/redoc" if settings.enable_api_docs else None,
    openapi_url="/openapi.json" if settings.enable_api_docs else None,
    lifespan=lifespan,
)

add_cors_middleware(app)
app.add_exception_handler(NavimaError, navima_exception_handler)


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
