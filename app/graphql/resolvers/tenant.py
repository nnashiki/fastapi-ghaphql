from app.graphql.types import tenant as type_tenant
from app import usecase


def my_tenant() -> type_tenant.Tenant:
    return usecase.tenant.read_my_tenant()

