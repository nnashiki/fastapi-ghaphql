from fastapi import APIRouter, Depends

from app.database import SuperSession, get_super_db
from app.dependencies import get_my_rights
from app.exceptions import NoRightsException
from app.models import Right
from app.schemas.tenant import (
    CreateTenantRequestBody,
    ReadManyTenantsRequestQueryParam,
    TenantResponse,
)
from app.services.authorization import has_any_rights
from app.usecases import tenant

router = APIRouter(
    prefix="/tenants",
    tags=["super tenants"],
)


@router.post("/")
def create_tenant(
    create_tenants_request_body: CreateTenantRequestBody,
    session: SuperSession = Depends(get_super_db),
    my_rights: list[Right] = Depends(get_my_rights),
) -> None:
    if not has_any_rights(my_rights=my_rights, require_rights=[Right(name="create.tenant")]):
        raise NoRightsException
    _ = tenant.create_tenant(
        session, name=create_tenants_request_body.name, service_plan_id=create_tenants_request_body.service_plan_id
    )
    return None


@router.get("/")
def read_many_tenants(
    session: SuperSession = Depends(get_super_db),
    query_param: ReadManyTenantsRequestQueryParam = Depends(),
    my_rights: list[Right] = Depends(get_my_rights),
) -> list[TenantResponse]:
    if not has_any_rights(my_rights=my_rights, require_rights=[Right(name="read.tenant")]):
        return []
    return tenant.read_many_tenants(session, name=query_param.name)
