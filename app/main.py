import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from .graphql.schema import schema


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def ping():
    return {"ping": "pong"}
