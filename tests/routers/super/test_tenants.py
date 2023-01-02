from app.models import Tenant
from tests.utilities import create_super_tenant_user, login


class TestCreate:
    def test_an_authenticated(self, session, app_client):
        _ = create_super_tenant_user(session)
        request_body = {"name": "test_tenant", "service_plan_id": 1}
        response = app_client.post("super/tenants/", json=request_body)
        assert response.status_code == 401
        assert response.json() == {"detail": "Not authenticated"}

    def test_success(self, session, app_client):
        super_tenant_user = create_super_tenant_user(session)
        request_body = {"name": "test_tenant", "service_plan_id": 1}
        login(app_client, super_tenant_user)
        response = app_client.post("super/tenants/", json=request_body)
        assert response.status_code == 200
        result = session.query(Tenant).filter(Tenant.name == "test_tenant").one()
        assert result.service_plan_id == 1
