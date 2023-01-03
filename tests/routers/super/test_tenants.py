from app.models import Tenant
from tests.utilities import create_super_tenant_user, free_tenant_users, login


class TestCreate:
    def test_an_authenticated(self, session, app_client):
        _ = create_super_tenant_user(session)
        request_body = {"name": "test_tenant", "service_plan_id": 1}
        response = app_client.post("super/tenants", json=request_body)
        assert response.status_code == 401
        assert response.json() == {"detail": "Not authenticated"}

    def test_success(self, session, app_client):
        super_tenant_user = create_super_tenant_user(session)
        request_body = {"name": "test_tenant", "service_plan_id": 1}
        login(app_client, super_tenant_user)
        response = app_client.post("super/tenants", json=request_body)
        assert response.status_code == 200
        result = session.query(Tenant).filter(Tenant.name == "test_tenant").one()
        assert result.service_plan_id == 1


class TestReadMany:
    def test_an_authenticated(self, session, app_client):
        _ = create_super_tenant_user(session)
        _ = free_tenant_users(session, "test_tenant")
        response = app_client.get("super/tenants/", params={"name": "test_tenant"})
        assert response.status_code == 401
        assert response.json() == {"detail": "Not authenticated"}

    def test_success(self, session, app_client):
        super_tenant_user = create_super_tenant_user(session)
        _ = free_tenant_users(session, "test_tenant")
        login(app_client, super_tenant_user)
        response = app_client.get("super/tenants/", params={"name": "test_tenant"})
        assert response.status_code == 200
        result_body = response.json()[0]
        assert len(result_body) == 5
        assert result_body["name"] == "test_tenant"
        assert result_body["service_plan_id"] == 1
