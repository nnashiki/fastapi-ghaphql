from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from ._base import BaseModel


class Right(BaseModel):
    __tablename__ = "rights"
    __table_args__ = (
        UniqueConstraint("name"),
        {"comment": "権限", "info": {}},
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    roles = relationship("Role", secondary="right_role_mappings", back_populates="rights")
