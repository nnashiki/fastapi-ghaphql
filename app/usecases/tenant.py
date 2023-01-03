import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.database import SuperSession
from app.models import Tenant


def read_my_tenant(db: Session) -> Tenant:
    tenant = db.query(Tenant).filter(Tenant.id == "de583d0a-e132-4c61-9b08-64685112046c").one()
    return tenant


def create_tenant(db: SuperSession, name: str, service_plan_id: int) -> Tenant:
    tenant = Tenant(name=name, service_plan_id=service_plan_id)
    db.add(tenant)
    db.commit()
    new_tenant = db.query(Tenant).filter(Tenant.name == name).one()
    return new_tenant


def read_tenant(db: Session, tenant_id: uuid.UUID) -> Tenant:
    tenant = db.get(Tenant, tenant_id)
    return tenant


def read_many_tenants(db: SuperSession, name: Optional[str]) -> list[Tenant]:
    tenants_query = db.query(Tenant)
    if name:
        tenants_query = tenants_query.filter(Tenant.name == name)
    return tenants_query.all()


def update_tenant(db: SuperSession, tenant_id: uuid.UUID, name: str) -> Tenant:
    tenant = db.get(Tenant, tenant_id)
    tenant.name = name
    db.commit()
    return tenant


def delete_tenant(db: SuperSession, tenant_id: uuid.UUID) -> None:
    tenant = db.get(Tenant, tenant_id)
    db.delete(tenant)
    db.commit()
    return
