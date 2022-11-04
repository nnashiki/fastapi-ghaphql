import uuid

import strawberry
from strawberry.types import Info

from app import usecase
from app.gql_context import CustomContext
from app.graphql.input.tenant import TenantCreateInput, TenantUpdateInput
from app.graphql.types.tenant import Tenant


@strawberry.type
class Mutation:
    @strawberry.field
    def create_tenant(self, ctx: Info[CustomContext, None], input_type: TenantCreateInput) -> Tenant:
        return usecase.tenant.create_tenant(db=ctx.context.db, name=input_type.name)

    @strawberry.field
    def update_tenant(self, ctx: Info[CustomContext, None], input_type: TenantUpdateInput) -> Tenant:
        return usecase.tenant.update_tenant(db=ctx.context.db, tenant_id=input_type.id, name=input_type.name)

    @strawberry.field
    def delete_tenant(self, ctx: Info[CustomContext, None], tenant_id: uuid.UUID) -> None:
        return usecase.tenant.delete_tenant(db=ctx.context.db, tenant_id=tenant_id)
