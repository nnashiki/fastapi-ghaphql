from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import Integer

from ._base import BaseModel


class RightRoleMapping(BaseModel):
    __tablename__ = "right_role_mappings"
    __table_args__ = (
        UniqueConstraint("right_id", "role_id"),
        {"comment": "権限ロールマッピング", "info": {}},
    )
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    right_id = Column(Integer, ForeignKey("rights.id", ondelete="CASCADE"), nullable=False)
