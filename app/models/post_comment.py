from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import BigInteger, String

from ._base import BaseModel


class PostComment(BaseModel):
    __tablename__ = "post_comments"
    __table_args__ = (
        UniqueConstraint("post_id", "tenant_user_id"),
        {"comment": "投稿コメント", "info": {}},
    )
    id = Column(BigInteger, primary_key=True)
    post_id = Column(BigInteger, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    tenant_user_id = Column(String(36), ForeignKey("tenant_users.id", ondelete="CASCADE"), nullable=False)
    comment = Column(String(255), nullable=False)

    post = relationship("Post", back_populates="post_comments")
    tenant_user = relationship("TenantUser", back_populates="post_comments")
