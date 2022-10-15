from app import models


class TestUsers:

    @staticmethod
    def _create_tenant_and_users(session):
        tenant = models.Tenant(name="新撰組")
        session.add(tenant)
        session.commit()

        team = models.Team(name="一番隊", tenant_id=tenant.id)
        session.add(team)
        session.commit()

        user = models.User(tenant_id=tenant.id, team_id=team.id, name="沖田総司")
        session.add(user)
        session.commit()

        user = session.query(models.User).filter(models.User.id == user.id).one()
        return user.tenant, user.team, user

    def test_create(self, session):
        tenant, team, user = self._create_tenant_and_users(session)
        assert user.name == "沖田総司"
        assert user.team.name == "一番隊"
        assert user.tenant.name == "新撰組"
        assert tenant.users[0].id == user.id

    def test_tenantを削除するとuserも削除される( # noqa
            self,
            session
        ):
        tenant, team, user = self._create_tenant_and_users(session)
        session.delete(team)
        user.team_id = None
        session.commit()
        session.delete(tenant)
        session.commit()
        assert session.query(models.User).count() == 0
