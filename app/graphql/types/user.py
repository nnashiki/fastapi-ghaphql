import uuid

import strawberry

from .team import Team
from .tenant import Tenant


@strawberry.type
class User:
    id: uuid.UUID
    name: str
    tenant: Tenant
    team: Team
