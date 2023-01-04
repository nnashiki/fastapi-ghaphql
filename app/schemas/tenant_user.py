from typing import Optional

from .base import AppRequestBaseModel, AppResponseBaseModel


class ReadTenantUsersRequestQueryParam(AppRequestBaseModel):
    name: Optional[str]


class TenantUserResponse(AppResponseBaseModel):
    id: str
    name: str
