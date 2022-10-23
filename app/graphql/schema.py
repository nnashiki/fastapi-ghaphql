import strawberry

from . import query, mutation

schema = strawberry.Schema(query=query.Query, mutation=mutation.Mutation)
