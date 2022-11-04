import strawberry

from .tenant import Tenant
from .user import User


@strawberry.type
class Post:
    id: int
    title: str
    detail: str
    tenant: Tenant
    posted_by: User
