from sqlalchemy.orm import Session

from app.models import Right


def has_any_rights(session: Session, my_rights: list[Right], require_rights: list[str]) -> bool:
    """
    必要権限のいずれかを持っているかどうかを判定する
    """
    _exist_rights(session, require_rights)
    my_right_names = [my_right.name for my_right in my_rights]
    return any([require_right in my_right_names for require_right in require_rights])


def _exist_rights(session: Session, rights: list[str]):
    counter = session.query(Right).filter(Right.name.in_(rights)).count()
    if len(set(rights)) != counter:
        raise ValueError("存在しない権限が指定されています")
