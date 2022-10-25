from strawberry.types import Info

from app import usecase
from app.gql_context import CustomContext
from app.graphql.types import tenant as type_tenant


def my_tenant(ctx: Info[CustomContext, None]) -> type_tenant.Tenant:
    return usecase.tenant.read_my_tenant(db=ctx.context.db)


def read_tenant(ctx: Info[CustomContext, None], tenant_id: str) -> type_tenant.Tenant:
    return usecase.tenant.read_tenant(db=ctx.context.db, tenant_id=tenant_id)
