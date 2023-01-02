from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_my_rights
from app.exceptions import NoRightsException
from app.models import Right
from app.schemas.tenant import CreateTenantRequestBody
from app.services.authorization import has_any_rights
from app.usecases import tenant

router = APIRouter(
    prefix="/tenants",
    tags=["super tenants"],
)


@router.post("/")
def create_tenant(
    create_tenants_request_body: CreateTenantRequestBody,
    session: Session = Depends(get_db),
    my_rights: list[Right] = Depends(get_my_rights),
):
    if not has_any_rights(my_rights=my_rights, require_rights=[Right(name="create.tenant")]):
        raise NoRightsException
    new = tenant.create_tenant(
        session, name=create_tenants_request_body.name, service_plan_id=create_tenants_request_body.service_plan_id
    )
    return new
