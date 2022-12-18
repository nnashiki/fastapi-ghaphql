import json

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.gql_context import get_context
from app.graphql.schema import schema
from app.routers import add_exception_handlers, api_router, super_router

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")

# REST
app.include_router(api_router)
app.include_router(super_router)
add_exception_handlers(app)

# OpenAPI Spec
openapi_spec = app.openapi()
with open("openapi.spec.json", "w") as f:
    json.dump(openapi_spec, f, indent=4, ensure_ascii=False)
