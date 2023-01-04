import datetime
import inspect

from pydantic import validator

from app.main import app
from app.schemas import base
from app_tests.utilities import free_tenant_users, login


class TestAppResponseBaseModel:
    def test_app_response_base_model(self):

        # TestModel has create_at with micro seconds
        test_model = base.AppResponseBaseModel(
            created_at=datetime.datetime(2022, 4, 1, 9, 0, 0, 111111, datetime.timezone(datetime.timedelta(hours=9))),
            updated_at=datetime.datetime(2022, 4, 1, 9, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=9))),
        )
        assert test_model.created_at == datetime.datetime(
            2022, 4, 1, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=0))
        )
        assert test_model.updated_at == datetime.datetime(
            2022, 4, 1, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=0))
        )
        assert test_model.json() == '{"created_at": "2022-04-01T00:00:00Z", "updated_at": "2022-04-01T00:00:00Z"}'


class TestAppRequestBaseModel:
    def test_normalizeを実装するとz_time_zoneに変換できる(self, session, app_client):  # noqa
        test_tenant_users = free_tenant_users(session, "test_tenant")
        login(app_client, test_tenant_users.tenant_member_1)

        class TestInputModel(base.AppRequestBaseModel):
            test_date_time: datetime.datetime

            _normalize_test_date_time = validator("test_date_time", allow_reuse=True)(base.normalize_datetime)

        api_path = "/api" + inspect.currentframe().f_code.co_name

        @app.post(api_path)
        def test_depends(request: TestInputModel):
            return {
                "result": request.test_date_time
                == datetime.datetime(2022, 4, 1, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=0)))
            }

        response = app_client.post(api_path, json={"testDateTime": "2022-04-01T09:00:00+09:00"})
        assert response.json()["result"] is True

    def test_camelでのデータを受け取ることができる(self, session, app_client):  # noqa
        test_tenant_users = free_tenant_users(session, "test_tenant")
        login(app_client, test_tenant_users.tenant_member_1)

        class TestInputModel(base.AppRequestBaseModel):
            test_date_time: datetime.datetime

        api_path = "/api" + inspect.currentframe().f_code.co_name

        @app.post(api_path)
        def test_depends(request: TestInputModel):

            return {
                "result": request.test_date_time
                == datetime.datetime(2022, 4, 1, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=0)))
            }

        response = app_client.post(api_path, json={"testDateTime": "2022-04-01T09:00:00+09:00"})
        assert response.json()["result"] is True
