import uuid

from sqlalchemy import Column, ForeignKey, MetaData, UniqueConstraint, func
from sqlalchemy.orm import (
    declarative_base,
    relationship,
)
from sqlalchemy.types import DateTime, Integer, String

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)


class Base:
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self) -> str:
        columns = ", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith("_")])
        return f"<{self.__class__.__name__}({columns})>"


BaseModel = declarative_base(metadata=metadata, cls=Base)


class Tenant(BaseModel):
    __tablename__ = "tenants"
    __table_args__ = (UniqueConstraint("name"), {})
    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)

    users = relationship(
        "User",
        back_populates="tenant",
        cascade="all",
        passive_deletes=True,
    )

    teams = relationship(
        "Team",
        order_by="Team.id",
        back_populates="tenant",
        cascade="all",
        passive_deletes=True,
    )


class Team(BaseModel):
    __tablename__ = "teams"
    __table_args__ = (UniqueConstraint("name"),  {"comment": "チーム", "info": {}},)
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    tenant_id = Column(String(36), ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)

    tenant = relationship("Tenant", back_populates="teams")
    users = relationship("User", back_populates="team", cascade="all", passive_deletes=True)


class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("name", "tenant_id"),
                      {"comment": "ユーザー", "info": {}},)
    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    tenant_id = Column(String(36), ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)

    tenant = relationship("Tenant", back_populates="users")
    team = relationship("Team", back_populates="users")
