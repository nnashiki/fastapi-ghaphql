from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["super users"],
)


@router.get("/")
async def read_users():
    return {"message": "Hello World"}
