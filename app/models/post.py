from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import BigInteger, String

from ._base import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"
    __table_args__ = (
        UniqueConstraint("title", "tenant_id"),
        {"comment": "投稿", "info": {}},
    )
    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    detail = Column(String(255), nullable=False)
    tenant_id = Column(String(36), ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    posted_by_id = Column(String(36), ForeignKey("tenant_users.id", ondelete="CASCADE"), nullable=False)

    tenant = relationship("Tenant", back_populates="posts")
    posted_by = relationship("TenantUser", back_populates="posts")
    post_likes = relationship("PostLike", back_populates="post", cascade="all", passive_deletes=True)
    post_comments = relationship("PostComment", back_populates="post", cascade="all", passive_deletes=True)
