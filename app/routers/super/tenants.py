from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_my_rights
from app.exceptions import NoRightsException
from app.models import Right
from app.services.authorization import has_any_rights
from app.usecases import tenant

router = APIRouter(
    prefix="/tenants",
    tags=["super tenants"],
)


@router.post("/", response_model=None)
def create_tenant(
    session: Session = Depends(get_db),
    my_rights: list[Right] = Depends(get_my_rights),
) -> None:
    if not has_any_rights(my_rights=my_rights, require_rights=[Right(name="create.tenant")]):
        raise NoRightsException
    _ = tenant.create_tenant(session, name="hoge")
    return None
