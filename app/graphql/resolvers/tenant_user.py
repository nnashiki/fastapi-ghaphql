from strawberry.types import Info

from app import usecase
from app.gql_context import CustomContext
from app.graphql.types import tenant_user


def read_users(ctx: Info[CustomContext, None]) -> list[tenant_user.TenantUser]:
    return usecase.tenant_user.read_users(db=ctx.context.db)
