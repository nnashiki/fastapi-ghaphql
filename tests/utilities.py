from typing import Optional

import jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.models import Tenant, TenantUser

from .conftest import CustomTestClient


def create_super_tenant_user(session: Session) -> TenantUser:
    """
    スーパーユーザーを作成する
    """
    tenant = Tenant(
        name="super_tenant",
        service_plan_id=777,
    )
    session.add(tenant)
    session.commit()

    super_user = TenantUser(
        tenant_id=tenant.id, name="super_tenant_user", idaas_id="00000000-0000-0000-0000-000000000000", role_id=777
    )
    session.add(super_user)
    session.commit()
    return super_user


class TestTenantUsers(BaseModel):
    tenant_member_1: Optional[TenantUser] = None
    tenant_member_2: Optional[TenantUser] = None
    tenant_admin_1: Optional[TenantUser] = None
    tenant_admin_2: Optional[TenantUser] = None

    class Config:
        arbitrary_types_allowed = True


def free_tenant_users(session: Session, tenant_name: str) -> TestTenantUsers:
    """
    free plan のテナントユーザーを作成する
    """
    tenant = Tenant(
        name=tenant_name,
        service_plan_id=1,
    )
    session.add(tenant)
    session.commit()

    free_member_user_1 = TenantUser(
        tenant_id=tenant.id,
        name=tenant_name + "_member_1",
        idaas_id="00000000-0000-0000-0000-000000000001",
        role_id=1,
    )
    session.add(free_member_user_1)
    session.commit()

    free_member_user_2 = TenantUser(
        tenant_id=tenant.id,
        name=tenant_name + "_member_2",
        idaas_id="00000000-0000-0000-0000-000000000002",
        role_id=1,
    )
    session.add(free_member_user_2)
    session.commit()

    free_admin_user_1 = TenantUser(
        tenant_id=tenant.id, name=tenant_name + "_admin_1", idaas_id="00000000-0000-0000-0000-000000000003", role_id=2
    )
    session.add(free_admin_user_1)
    session.commit()

    free_admin_user_2 = TenantUser(
        tenant_id=tenant.id, name=tenant_name + "_admin_2", idaas_id="00000000-0000-0000-0000-000000000004", role_id=2
    )
    session.add(free_admin_user_2)
    session.commit()

    return TestTenantUsers(
        tenant_member_1=free_member_user_1,
        tenant_member_2=free_member_user_2,
        tenant_admin_1=free_admin_user_1,
        tenant_admin_2=free_admin_user_2,
    )


def login(app_client: CustomTestClient, tenant_user: TenantUser):
    app_client.token = jwt.encode({"idaas_id": str(tenant_user.idaas_id)}, key="private_key", algorithm="HS256")
    return app_client
