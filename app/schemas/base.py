import datetime
from datetime import timezone

import humps
from pydantic import BaseModel, validator


def convert_datetime_to_iso_8601_with_z_suffix(dt: datetime.datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _convert_to_utc_datetime(dt: datetime.datetime) -> datetime.datetime:
    return dt.astimezone(tz=timezone.utc)


def _round_datetime(dt: datetime.datetime) -> datetime.datetime:
    return dt.replace(microsecond=0)


def normalize_datetime(dt: datetime.datetime) -> datetime.datetime:
    dt = _convert_to_utc_datetime(dt)
    dt = _round_datetime(dt)
    return dt


def _to_camel(string: str) -> str:
    return humps.camelize(string)


class AppResponseBaseModel(BaseModel):
    created_at: datetime.datetime
    updated_at: datetime.datetime

    # validators
    _normalize_created_at = validator("created_at", allow_reuse=True)(normalize_datetime)
    _normalize_updated_at = validator("updated_at", allow_reuse=True)(normalize_datetime)

    class Config:
        orm_mode = True
        alias_generator = _to_camel
        allow_population_by_field_name = True
        json_encoders = {
            # custom output conversion for datetime
            datetime.datetime: convert_datetime_to_iso_8601_with_z_suffix
        }
