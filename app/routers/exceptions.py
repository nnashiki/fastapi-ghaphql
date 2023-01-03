from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import NoRightsException


def add_exception_handlers(app):
    """
    エクセプションハンドラーはこの関数の中に追加していく
    """

    @app.exception_handler(NoRightsException)
    async def NoRightsException_handler(request: Request, exc: NoRightsException):
        return JSONResponse(status_code=403, content=exc.body)
