import strawberry

from app.graphql.types.tenant import Tenant
from app import usecase


@strawberry.type
class Mutation:
    @strawberry.field
    def create_tenant(self, name: str) -> Tenant:
        return usecase.tenant.create_tenant(name)
