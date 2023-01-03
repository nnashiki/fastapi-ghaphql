import datetime

from app.schemas import base


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
