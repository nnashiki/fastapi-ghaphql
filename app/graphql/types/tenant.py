import uuid

import strawberry


@strawberry.type
class Tenant:
    id: uuid.UUID
    name: str
