from strawberry.types import Info

from app import usecases
from app.gql_context import CustomContext
from app.graphql.types import tenant as type_tenant


def my_tenant(ctx: Info[CustomContext, None]) -> type_tenant.Tenant:
    return usecases.tenant.read_my_tenant(session=ctx.context.db)


def read_tenant(ctx: Info[CustomContext, None], tenant_id: str) -> type_tenant.Tenant:
    return usecases.tenant.read_tenant(session=ctx.context.db, tenant_id=tenant_id)
