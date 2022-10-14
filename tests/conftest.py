import pytest
from app import models, database


def init_tables(session):
    # 初期化
    session.query(models.User).delete()
    session.query(models.Tenant).delete()
    session.commit()


@pytest.fixture()
def session():

    sa_session = database.session()
    try:
        # テストメソッドが使うためのsession
        init_tables(sa_session)
        yield sa_session

    finally:
        sa_session.close()
