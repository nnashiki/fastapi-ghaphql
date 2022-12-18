from fastapi import APIRouter

from app import exceptions

router = APIRouter(
    prefix="/users",
    tags=["api users"],
)


@router.get("/")
async def read_users():
    return {"message": "Hello World"}


@router.get("/exception")
async def read_users_exception():
    raise exceptions.MyException()
