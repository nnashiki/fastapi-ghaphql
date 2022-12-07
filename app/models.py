import uuid

from sqlalchemy import Column, ForeignKey, MetaData, UniqueConstraint, func
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.types import BigInteger, DateTime, Integer, String

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


class ServicePlan(BaseModel):
    __tablename__ = "service_plans"
    __table_args__ = (
        UniqueConstraint("name"),
        {"comment": "サービスプラン", "info": {}},
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    tenants = relationship("Tenant", back_populates="service_plan")


class Right(BaseModel):
    __tablename__ = "rights"
    __table_args__ = (
        UniqueConstraint("name"),
        {"comment": "権限", "info": {}},
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


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


class RightRoleMapping(BaseModel):
    __tablename__ = "right_role_mappings"
    __table_args__ = (
        UniqueConstraint("right_id", "role_id"),
        {"comment": "権限ロールマッピング", "info": {}},
    )
    id = Column(Integer, primary_key=True)
    right_id = Column(Integer, ForeignKey("rights.id", ondelete="CASCADE"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)


class Tenant(BaseModel):
    __tablename__ = "tenants"
    __table_args__ = (UniqueConstraint("name"), {})
    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    service_plan_id = Column(Integer, ForeignKey("service_plans.id"), nullable=False)

    service_plan = relationship("ServicePlan", back_populates="tenants")

    users = relationship(
        "User",
        back_populates="tenant",
        cascade="all",
        passive_deletes=True,
    )

    posts = relationship("Post", back_populates="tenant", cascade="all", passive_deletes=True)


class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = (
        UniqueConstraint("name", "tenant_id"),
        {"comment": "ユーザー", "info": {}},
    )
    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    tenant_id = Column(String(36), ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)

    tenant = relationship("Tenant", back_populates="users")
    posts = relationship("Post", back_populates="posted_by", cascade="all", passive_deletes=True)


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
    posted_by_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    tenant = relationship("Tenant", back_populates="posts")
    posted_by = relationship("User", back_populates="posts")
