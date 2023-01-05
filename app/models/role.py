from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from ._base import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"
    __table_args__ = (
        UniqueConstraint("name"),
        {
            "comment": "ロール(1:super, 10:basic plan member, 11:basic plan Admin, 20: premium plan member,  21: premium plan admin 99:停止ユーザー",
            "info": {},
        },
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    service_plan_id = Column(Integer, ForeignKey("service_plans.id"), nullable=False)

    service_plan = relationship("ServicePlan", back_populates="roles")
    tenant_users = relationship("TenantUser", back_populates="role")
    rights = relationship("Right", secondary="right_role_mappings", back_populates="roles")
