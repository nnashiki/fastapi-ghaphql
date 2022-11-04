import strawberry

from app.graphql import resolvers
from app.graphql.types.tenant import Tenant
from app.graphql.types.user import User


@strawberry.type
class Query:
    my_tenant: Tenant = strawberry.field(resolver=resolvers.tenant.my_tenant)

    tenant: Tenant = strawberry.field(resolver=resolvers.tenant.read_tenant)

    users: list[User] = strawberry.field(resolver=resolvers.user.read_users)
