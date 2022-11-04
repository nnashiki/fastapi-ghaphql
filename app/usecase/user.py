from sqlalchemy.orm import Session

from app.models import User


def read_users(db: Session) -> list[User]:
    users = db.query(User).all()
    return users
