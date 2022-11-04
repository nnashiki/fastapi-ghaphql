import uuid

import strawberry


@strawberry.input
class TenantCreateInput:
    name: str


@strawberry.input
class TenantUpdateInput:
    id: uuid.UUID
    name: str
