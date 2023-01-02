from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://dbuser:password@db/mydb", encoding="utf-8")
_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = _session_local()
    try:
        yield db
    finally:
        db.close()
