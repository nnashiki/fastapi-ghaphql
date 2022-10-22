import strawberry

from . import query

schema = strawberry.Schema(query=query.Query)
