from strawberry.types import Info

from app import usecases
from app.gql_context import CustomContext
from app.graphql.types import post as type_post


def read_posts(ctx: Info[CustomContext, None]) -> list[type_post.Post]:
    return usecases.post.read_posts(db=ctx.context.db)
