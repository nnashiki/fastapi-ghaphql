from app import models


def create_tenant_and_users(session) -> (models.Tenant, models.TenantUser):
    tenant = models.Tenant(name="新撰組", service_plan_id=1)
    session.add(tenant)
    session.commit()

    user = models.TenantUser(
        tenant_id=tenant.id,
        name="沖田総司",
        idaas_id="00000000-0000-0000-0000-000000000000",
        role_id=1,
    )
    session.add(user)
    session.commit()
    return user.tenant, user
