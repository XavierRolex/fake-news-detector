from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

class InvalidTextException(Exception):
    def __init__(self, detail: str = "Invalid input text."):
        self.detail = detail

async def invalid_text_exception_handler(request: Request, exc: InvalidTextException):
    logger.warning(f"InvalidTextException: {exc.detail}")
    return JSONResponse(
        status_code=422,
        content={"error": exc.detail},
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {repr(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error. Please try again later."},
    )
