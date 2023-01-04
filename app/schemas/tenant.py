from .base import AppRequestBaseModel, AppResponseBaseModel


class CreateTenantRequestBody(AppRequestBaseModel):
    name: str
    service_plan_id: int


class ReadTenantsRequestQueryParam(AppRequestBaseModel):
    name: str


class UpdateTenantRequestBody(AppRequestBaseModel):
    name: str


class TenantResponse(AppResponseBaseModel):
    id: str
    name: str
    service_plan_id: int
