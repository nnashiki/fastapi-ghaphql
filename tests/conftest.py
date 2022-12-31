import pytest
from fastapi.testclient import TestClient

from app import database, models
from app.main import app


def init_tables(session):
    # 初期化
    session.query(models.TenantUser).delete()
    session.query(models.Tenant).delete()
    session.commit()


@pytest.fixture()
def session():
    """
    テストメソッドが使うためのsession
    """

    sa_session = database.get_session_maker()()
    try:
        init_tables(sa_session)
        yield sa_session

    finally:
        sa_session.close()


class CustomTestClient(TestClient):
    token = ""

    def get(self, *args, **kwargs):
        if self.token:
            if "headers" in kwargs.keys():
                kwargs["headers"].update({"Authorization": f"Bearer {self.token}"})
            else:
                kwargs["headers"] = {"Authorization": f"Bearer {self.token}"}
            return super().get(*args, **kwargs)
        else:
            return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.token:
            if "headers" in kwargs.keys():
                kwargs["headers"].update({"Authorization": f"Bearer {self.token}"})
            else:
                kwargs["headers"] = {"Authorization": f"Bearer {self.token}"}
            return super().post(*args, **kwargs)
        else:
            return super().post(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.token:
            if "headers" in kwargs.keys():
                kwargs["headers"].update({"Authorization": f"Bearer {self.token}"})
            else:
                kwargs["headers"] = {"Authorization": f"Bearer {self.token}"}
            return super().delete(*args, **kwargs)
        else:
            return super().delete(*args, **kwargs)

    def patch(self, *args, **kwargs):
        if self.token:
            if "headers" in kwargs.keys():
                kwargs["headers"].update({"Authorization": f"Bearer {self.token}"})
            else:
                kwargs["headers"] = {"Authorization": f"Bearer {self.token}"}
            return super().patch(*args, **kwargs)
        else:
            return super().patch(*args, **kwargs)

    def put(self, *args, **kwargs):
        if self.token:
            if "headers" in kwargs.keys():
                kwargs["headers"].update({"Authorization": f"Bearer {self.token}"})
            else:
                kwargs["headers"] = {"Authorization": f"Bearer {self.token}"}
            return super().put(*args, **kwargs)
        else:
            return super().put(*args, **kwargs)


@pytest.fixture()
def app_client():
    yield CustomTestClient(app=app)
