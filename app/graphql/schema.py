import strawberry

from . import mutation, query

schema = strawberry.Schema(query=query.Query, mutation=mutation.Mutation)
