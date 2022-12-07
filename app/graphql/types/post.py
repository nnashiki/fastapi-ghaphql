import strawberry

from .tenant import Tenant
from .tenant_user import TenantUser


@strawberry.type
class Post:
    id: int
    title: str
    detail: str
    tenant: Tenant
    posted_by: TenantUser
