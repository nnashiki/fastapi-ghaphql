from app.models import Right
from app.services.authorization import has_any_rights


class TestHasAnyRights:
    def test_has_any_rights(self):
        my_rights = [Right(name="right1"), Right(name="right2")]
        require_rights = [Right(name="right2"), Right(name="right3")]
        assert has_any_rights(my_rights, require_rights) is True

    def test_has_any_rights_false(self):
        my_rights = [Right(name="right1"), Right(name="right2")]
        require_rights = [Right(name="right3"), Right(name="right4")]
        assert has_any_rights(my_rights, require_rights) is False
