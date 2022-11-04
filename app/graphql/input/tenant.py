import strawberry


@strawberry.input
class TenantInput:
    name: str
