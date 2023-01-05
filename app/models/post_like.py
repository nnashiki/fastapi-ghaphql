from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import BigInteger, String

from ._base import BaseModel


class PostLike(BaseModel):
    __tablename__ = "post_likes"
    __table_args__ = (
        UniqueConstraint("post_id", "tenant_user_id"),
        {"comment": "投稿いいね", "info": {}},
    )
    id = Column(BigInteger, primary_key=True)
    post_id = Column(BigInteger, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    tenant_user_id = Column(String(36), ForeignKey("tenant_users.id", ondelete="CASCADE"), nullable=False)

    post = relationship("Post", back_populates="post_likes")
    tenant_user = relationship("TenantUser", back_populates="post_likes")
