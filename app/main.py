from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.gql_context import get_context
from app.graphql.schema import schema

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def ping():
    return {"ping": "pong"}
