import strawberry


@strawberry.type
class Team:
    id: int
    name: str
