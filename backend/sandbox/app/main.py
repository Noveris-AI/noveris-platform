import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

ENABLE_API_DOCS = os.getenv("ENABLE_API_DOCS", "true").lower() == "true"

app = FastAPI(
    title="Navima Sandbox",
    version="0.1.0",
    docs_url="/docs" if ENABLE_API_DOCS else None,
    redoc_url="/redoc" if ENABLE_API_DOCS else None,
    openapi_url="/openapi.json" if ENABLE_API_DOCS else None,
)


@app.get("/health/live", tags=["health"])
async def health_live() -> JSONResponse:
    return JSONResponse(content={"status": "ok"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)


@app.get("/health/ready", tags=["health"])
async def health_ready() -> JSONResponse:
    return JSONResponse(content={"status": "ok"})
