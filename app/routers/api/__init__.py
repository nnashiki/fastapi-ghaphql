from fastapi import APIRouter

from .tenant_users import router as tenant_user_router

router = APIRouter(
    prefix="/api",
)
router.include_router(tenant_user_router)
