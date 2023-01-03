from typing import Optional

from pydantic import BaseModel

from .base import AppResponseBaseModel


class ReadTenantUsersRequestQueryParam(BaseModel):
    name: Optional[str]


class TenantUserResponse(AppResponseBaseModel):
    id: str
    name: str
