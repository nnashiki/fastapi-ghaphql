from tests.utilities import create_super_tenant_user, login


class TestCreate:
    def test_an_authenticated(self, session, app_client):
        _ = create_super_tenant_user(session)
        response = app_client.post("super/tenants/", json={})
        assert response.status_code == 401
        assert response.json() == {"detail": "Not authenticated"}

    def test_success(self, session, app_client):
        super_tenant_user = create_super_tenant_user(session)
        login(app_client, super_tenant_user)
        response = app_client.post("super/tenants/", json={})
        assert response.status_code == 200
        assert response.json() is None
