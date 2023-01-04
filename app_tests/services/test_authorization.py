import pytest

from app.models import Right
from app.services.authorization import has_any_rights


class TestHasAnyRights:
    def test_存在しない権限を指定した場合に例外が発生する(self, session):  # noqa
        my_rights = [Right(name="right1"), Right(name="right2")]
        require_rights = ["right2", "right3"]
        with pytest.raises(ValueError) as e:
            has_any_rights(session, my_rights, require_rights)
        assert str(e.value) == "存在しない権限が指定されています"

    def test_has_any_rights_true(self, session):
        my_rights = [Right(name="read.tenant")]
        require_rights = ["create.tenant", "read.tenant"]
        assert has_any_rights(session, my_rights, require_rights) is True

    def test_has_any_rights_false(self, session):
        my_rights = [Right(name="read.tenant")]
        require_rights = ["create.tenant"]
        assert has_any_rights(session, my_rights, require_rights) is False
