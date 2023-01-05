from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from ._base import BaseModel


class ServicePlan(BaseModel):
    __tablename__ = "service_plans"
    __table_args__ = (
        UniqueConstraint("name"),
        {"comment": "サービスプラン", "info": {}},
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    tenants = relationship("Tenant", back_populates="service_plan")
    roles = relationship("Role", back_populates="service_plan")
