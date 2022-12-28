from sqlalchemy.orm import Session

from app.models import TenantUser


def read_users(db: Session) -> list[TenantUser]:
    tenant_users = db.query(TenantUser).all()
    return tenant_users
