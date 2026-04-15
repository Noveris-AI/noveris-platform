from collections.abc import AsyncIterator

from fastapi import FastAPI
from navima_shared.db.session import engine

from app.core.logging import configure_logging


def on_startup() -> None:
    configure_logging(log_level="INFO")


async def on_shutdown() -> None:
    await engine.dispose()


async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    on_startup()
    yield
    await on_shutdown()
