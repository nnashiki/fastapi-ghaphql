from tests.util import create_tenant_and_users


class TestTenantQueries:
    def test_tenant_query_with_id(self, session, app_client):
        tenant, team, user = create_tenant_and_users(session)
        query = """
                    query {
                      tenant(tenantId: "%s") {
                        id
                        name
                      }
                    }""" % (
            tenant.id
        )

        response = app_client.post("/graphql", json={"query": query})
        assert response.status_code == 200
        result = response.json()

        assert result.get("error") is None
        assert result["data"]["tenant"]["id"] == tenant.id
        assert result["data"]["tenant"]["name"] == tenant.name
