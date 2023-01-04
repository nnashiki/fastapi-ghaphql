import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.cruds import tenant as cruds_tenant
from app.database import SuperSession
from app.models import Tenant


def create_tenant(session: SuperSession, name: str, service_plan_id: int) -> Tenant:
    return cruds_tenant.create_tenant(session, name, service_plan_id)


def read_tenant(session: Session, tenant_id: uuid.UUID) -> Tenant:
    return cruds_tenant.read_tenant(session, tenant_id)


def read_tenants(session: SuperSession, name: Optional[str]) -> list[Tenant]:
    return cruds_tenant.read_tenants(session, name)


def update_tenant(session: SuperSession, tenant_id: uuid.UUID, name: str) -> Tenant:
    return cruds_tenant.update_tenant(session, tenant_id, name)


def delete_tenant(session: SuperSession, tenant_id: uuid.UUID) -> bool:
    return cruds_tenant.delete_tenant(session, tenant_id)
