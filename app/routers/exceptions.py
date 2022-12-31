from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import MyException, NoRightsException


def add_exception_handlers(app):
    @app.exception_handler(MyException)
    async def MyException_handler(request: Request, exc: MyException):
        return JSONResponse(status_code=500, content=exc.body)

    @app.exception_handler(NoRightsException)
    async def NoRightsException_handler(request: Request, exc: NoRightsException):
        return JSONResponse(status_code=403, content=exc.body)
