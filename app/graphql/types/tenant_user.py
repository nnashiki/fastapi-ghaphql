import uuid

import strawberry

from .tenant import Tenant


@strawberry.type
class TenantUser:
    id: uuid.UUID
    name: str
    tenant: Tenant
