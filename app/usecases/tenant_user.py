from typing import Optional

from sqlalchemy.orm import Session

from app.models import TenantUser


def read_users(session: Session, name: Optional[str]) -> list[TenantUser]:
    query = session.query(TenantUser)
    if name:
        query = query.filter(TenantUser.name == name)
    result = query.all()
    return result
