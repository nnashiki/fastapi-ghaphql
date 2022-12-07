import pytest
from fastapi.testclient import TestClient

from app import database, models
from app.main import app


def init_tables(session):
    # 初期化
    session.query(models.User).delete()
    session.query(models.Tenant).delete()
    session.query(models.ServicePlan).delete()
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


@pytest.fixture()
def app_client():
    yield TestClient(app=app)
