from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://dbuser:password@db/mydb", encoding="utf-8", echo=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
