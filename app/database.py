from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class SuperSession(Session):
    pass


class TenantSession(Session):
    """
    type hint 用途に利用する
    Type Guard には利用しない
    """

    pass


engine = create_engine("mysql+pymysql://dbuser:password@db/mydb", encoding="utf-8")
_tenant_session = sessionmaker(class_=TenantSession, autocommit=False, autoflush=False, bind=engine)
_super_session = sessionmaker(class_=SuperSession, autocommit=False, autoflush=False, bind=engine)


def get_tenant_db() -> TenantSession:
    db = _tenant_session()
    try:
        yield db
    finally:
        db.close()


def get_super_db() -> SuperSession:
    db = _super_session()
    try:
        yield db
    finally:
        db.close()
