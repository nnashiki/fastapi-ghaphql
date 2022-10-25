from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_engine = create_engine("mysql+pymysql://dbuser:password@db/mydb", encoding="utf-8", echo=True)
_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def get_db():
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
