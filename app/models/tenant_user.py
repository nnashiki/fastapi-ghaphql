import uuid

from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from ._base import BaseModel


class TenantUser(BaseModel):
    __tablename__ = "tenant_users"
    __table_args__ = (
        UniqueConstraint("name", "tenant_id"),
        {"comment": "ユーザー", "info": {}},
    )
    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    idaas_id = Column(String(36), nullable=False)
    tenant_id = Column(String(36), ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    tenant = relationship("Tenant", back_populates="tenant_users")
    role = relationship("Role", back_populates="tenant_users")
    posts = relationship("Post", back_populates="posted_by", cascade="all", passive_deletes=True)
    post_likes = relationship(
        "PostLike", back_populates="tenant_user", cascade="all", passive_deletes=True, lazy="joined"
    )
    post_comments = relationship(
        "PostComment", back_populates="tenant_user", cascade="all", passive_deletes=True, lazy="joined"
    )
