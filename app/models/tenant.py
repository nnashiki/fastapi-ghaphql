import uuid

from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from ._base import BaseModel


class Tenant(BaseModel):
    __tablename__ = "tenants"
    __table_args__ = (UniqueConstraint("name"), {})
    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    service_plan_id = Column(Integer, ForeignKey("service_plans.id"), nullable=False)

    service_plan = relationship("ServicePlan", back_populates="tenants")

    tenant_users = relationship(
        "TenantUser",
        back_populates="tenant",
        cascade="all",
        passive_deletes=True,
    )

    posts = relationship("Post", back_populates="tenant", cascade="all", passive_deletes=True)
