from app import models


class TestUsers:

    @staticmethod
    def _create_tenant_and_users(session):
        tenant = models.Tenant(name="新撰組")
        session.add(tenant)
        session.commit(),
        user = models.User(tenant_id=tenant.id, name="近藤勇")
        session.add(user)
        session.commit()

        user = session.query(models.User).filter(models.User.id == user.id).one()
        return tenant, user

    def test_create(self, session):
        tenant, user = self._create_tenant_and_users(session)
        assert user.name == "近藤勇"
        assert user.tenant_id == tenant.id
        assert user.tenant.id == tenant.id
        assert user.tenant.name == "新撰組"
        assert tenant.users[0].id == user.id

    def test_tenantを削除するとuserも削除される( # noqa
            self,
            session
        ):
        tenant, user = self._create_tenant_and_users(session)
        session.delete(tenant)
        session.commit()
        assert session.query(models.User).count() == 0
