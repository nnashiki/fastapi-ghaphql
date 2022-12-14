import strawberry

from app.graphql import resolvers
from app.graphql.types.post import Post
from app.graphql.types.tenant import Tenant
from app.graphql.types.tenant_user import TenantUser


@strawberry.type
class Query:
    tenant_me: Tenant = strawberry.field(resolver=resolvers.tenant.my_tenant)

    tenant: Tenant = strawberry.field(resolver=resolvers.tenant.read_tenant)

    tenant_users: list[TenantUser] = strawberry.field(resolver=resolvers.tenant_user.read_users)

    posts: list[Post] = strawberry.field(resolver=resolvers.post.read_posts)
