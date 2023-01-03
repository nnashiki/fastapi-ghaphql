from tests.utilities import free_tenant_users, login


class TestGet:
    def test_an_authenticated(self, session, app_client):
        _ = free_tenant_users(session, "test_tenant")
        response = app_client.get("api/tenant-users", params={})
        assert response.status_code == 401
        assert response.json() == {"detail": "Not authenticated"}

    def test_success(self, session, app_client):
        test_tenant_users = free_tenant_users(session, "test_tenant")
        login(app_client, test_tenant_users.tenant_member_1)
        response = app_client.get("api/tenant-users", params={})
        assert response.status_code == 200
        result = response.json()
        assert len(result) == 4
        tenant_user_names = [
            "test_tenant_member_1",
            "test_tenant_member_2",
            "test_tenant_admin_1",
            "test_tenant_admin_2",
        ]
        assert result[0]["name"] in tenant_user_names
        assert result[1]["name"] in tenant_user_names
        assert result[2]["name"] in tenant_user_names
        assert result[3]["name"] in tenant_user_names
