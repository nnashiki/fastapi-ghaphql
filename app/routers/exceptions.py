from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import MyException


def add_exception_handlers(app):
    @app.exception_handler(MyException)
    async def MyException_handler(request: Request, exc: MyException):
        print("MyException occured!!!")
        return JSONResponse(status_code=500, content=exc.body)
