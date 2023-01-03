from pydantic import BaseModel

from .base import AppResponseBaseModel


class CreateTenantRequestBody(BaseModel):
    name: str
    service_plan_id: int


class ReadTenantsRequestQueryParam(BaseModel):
    name: str


class UpdateTenantRequestBody(BaseModel):
    name: str


class TenantResponse(AppResponseBaseModel):
    id: str
    name: str
    service_plan_id: int
