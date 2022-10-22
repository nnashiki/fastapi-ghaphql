import strawberry

from app.graphql import resolvers
from app.graphql.types.tenant import Tenant


@strawberry.type
class Query:
    my_tenants: Tenant = strawberry.field(resolver=resolvers.tenant.my_tenant)
