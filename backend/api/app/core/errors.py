from typing import Any

from fastapi import Request, status
from fastapi.responses import JSONResponse


class NavimaError(Exception):
    """Base exception for Navima API."""

    def __init__(
        self,
        code: str,
        message: str,
        detail: dict[str, Any] | None = None,
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ) -> None:
        self.code = code
        self.message = message
        self.detail = detail or {}
        self.status_code = status_code
        super().__init__(message)


def navima_exception_handler(request: Request, exc: NavimaError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.code,
            "message": exc.message,
            "detail": exc.detail,
        },
    )
