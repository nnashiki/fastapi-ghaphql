from fastapi import APIRouter, Depends

from app import exceptions, usecases
from app.database import TenantSession, get_tenant_db
from app.dependencies import get_my_rights
from app.models import Right
from app.schemas.tenant_user import ReadTenantUsersRequestQueryParam, TenantUserResponse
from app.services.authorization import has_any_rights

router = APIRouter(
    prefix="/tenant-users",
    tags=["tenant users"],
)


@router.get("", response_model=list[TenantUserResponse])
async def read_users(
    query_param: ReadTenantUsersRequestQueryParam = Depends(),
    session: TenantSession = Depends(get_tenant_db),
    my_rights: list[Right] = Depends(get_my_rights),
):
    if not has_any_rights(session=session, my_rights=my_rights, require_rights=["read.tenant_user"]):
        raise exceptions.NoRightsException
    return usecases.tenant_user.read_users(session=session, name=query_param.name)
