from strawberry.types import Info

from app import usecase
from app.gql_context import CustomContext
from app.graphql.types import user as type_user


def read_users(ctx: Info[CustomContext, None]) -> list[type_user.User]:
    return usecase.user.read_users(db=ctx.context.db)
