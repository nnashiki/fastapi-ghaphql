from app.models import Right


def has_any_rights(my_rights: list[Right], require_rights: list[Right]) -> bool:
    """
    必要権限のいずれかを持っているかどうかを判定する
    """
    my_right_names = [my_right.name for my_right in my_rights]
    return any([require_right.name in my_right_names for require_right in require_rights])
