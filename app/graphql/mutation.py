import strawberry
from strawberry.types import Info

from app import usecase
from app.gql_context import CustomContext
from app.graphql.input.tenant import TenantInput
from app.graphql.types.tenant import Tenant


@strawberry.type
class Mutation:
    @strawberry.field
    def create_tenant(self, ctx: Info[CustomContext, None], input_type: TenantInput) -> Tenant:
        return usecase.tenant.create_tenant(db=ctx.context.db, name=input_type.name)
