from fastapi import APIRouter

from .tenants import router as tenants_router
from .users import router as users_router

router = APIRouter(
    prefix="/super",
)
router.include_router(users_router)
router.include_router(tenants_router)
