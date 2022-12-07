from app import models
from tests.util import create_tenant_and_users


class TestUsers:
    def test_create(self, session):
        tenant, tenant_user = create_tenant_and_users(session)
        assert tenant_user.name == "沖田総司"
        assert tenant.tenant_users[0].id == tenant_user.id

    def test_tenantを削除するとuserも削除される(self, session):  # noqa
        tenant, tenant_user = create_tenant_and_users(session)
        session.delete(tenant)
        session.commit()
        assert session.query(models.TenantUser).count() == 0
