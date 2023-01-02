from pydantic import BaseModel


class CreateTenantRequestBody(BaseModel):
    name: str
    service_plan_id: int


class ReadTenantRequestQueryParam(BaseModel):
    pass


class UpdateTenantRequestBody(BaseModel):
    name: str


class TenantResponse(BaseModel):
    id: str
    name: str
    service_plan_id: int