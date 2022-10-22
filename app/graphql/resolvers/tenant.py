from app import routers
from app.graphql.types import tenant as type_tenant


def my_tenant() -> type_tenant.Tenant:
    return routers.my_tenant.read_my_tenant()
