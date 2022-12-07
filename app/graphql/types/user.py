import uuid

import strawberry

from .tenant import Tenant


@strawberry.type
class User:
    id: uuid.UUID
    name: str
    tenant: Tenant
