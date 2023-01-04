import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker

from app import models
from app.database import engine, get_tenant_db
from app.main import app


def _init_tables(session):
    # 初期化
    session.query(models.TenantUser).delete()
    session.query(models.Tenant).delete()
    session.commit()


@pytest.fixture(scope="function")
def session():
    """
    テストメソッドが使うためのsession
    """

    function_scope = uuid.uuid4().hex
    TestingSessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine),
        scopefunc=lambda: function_scope,
    )

    def override_get_db():
        # API側で使う session id を同じにする(scoped_session)
        testing_session_local = TestingSessionLocal()
        try:
            yield testing_session_local
            testing_session_local.commit()
        except SQLAlchemyError:
            testing_session_local.rollback()

    app.dependency_overrides[get_tenant_db] = override_get_db

    sa_session = TestingSessionLocal()
    try:
        _init_tables(sa_session)
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
