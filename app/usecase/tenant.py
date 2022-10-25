from sqlalchemy.orm import Session

from app.models import Tenant


def read_my_tenant(db: Session) -> Tenant:
    tenant = db.query(Tenant).filter(Tenant.id == "de583d0a-e132-4c61-9b08-64685112046c").one()
    return tenant


def create_tenant(db: Session, name: str) -> Tenant:
    tenant = Tenant(name=name)
    db.add(tenant)
    db.commit()
    tenant = db.query(Tenant).filter(Tenant.name == name).one()
    return tenant


def read_tenant(db: Session, tenant_id: str) -> Tenant:
    tenant = db.get(Tenant, tenant_id)
    return tenant
