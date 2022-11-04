from app import models
from tests.util import create_tenant_and_users


class TestUsers:
    def test_create(self, session):
        tenant, team, user = create_tenant_and_users(session)
        assert user.name == "沖田総司"
        assert user.team.name == "一番隊"
        assert user.tenant.name == "新撰組"
        assert tenant.users[0].id == user.id

    def test_tenantを削除するとuserも削除される(self, session):  # noqa
        tenant, team, user = create_tenant_and_users(session)
        session.delete(team)
        user.team_id = None
        session.commit()
        session.delete(tenant)
        session.commit()
        assert session.query(models.User).count() == 0
