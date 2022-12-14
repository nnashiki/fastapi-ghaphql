from typing import Optional

from sqlalchemy.orm import Session

from app.cruds import tenant_user as cruds_tenant_user
from app.models import TenantUser


def read_users(session: Session, name: Optional[str]) -> list[TenantUser]:
    return cruds_tenant_user.read_users(session, name)
