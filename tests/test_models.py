from app import models
from tests.util import create_tenant_and_users


class TestUsers:
    def test_create(self, session):
        tenant, user = create_tenant_and_users(session)
        assert user.name == "沖田総司"
        assert tenant.users[0].id == user.id

    def test_tenantを削除するとuserも削除される(self, session):  # noqa
        tenant, user = create_tenant_and_users(session)
        session.delete(tenant)
        session.commit()
        assert session.query(models.User).count() == 0
