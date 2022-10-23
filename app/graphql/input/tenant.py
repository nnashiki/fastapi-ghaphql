import strawberry


@strawberry.type
class TenantInput:
    name: str
