from sqlalchemy.orm import Session

from app.models import Post


def read_posts(db: Session) -> list[Post]:
    posts = db.query(Post).all()
    return posts
