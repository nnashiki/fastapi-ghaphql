from typing import Any

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Right, TenantUser


def get_jwt_payload_for_unit_test(token: str) -> dict[str, Any]:
    """
    JWTトークンからpayloadを取得する
    """
    _ = token
    return {"uuid": "00000000-0000-0000-0000-000000000000"}


def get_user_from_jwt_payload(
    payload: dict[str, Any] = Depends(get_jwt_payload_for_unit_test),
    session: Session = Depends(get_db),
) -> TenantUser:
    """
    JWTトークン payload からユーザーを取得する
    """

    user = session.query(TenantUser).filter(TenantUser.uuid == payload["uuid"]).one()
    # ここに様々なバリデーションが入る
    return user


def get_my_rights(
    me: TenantUser = Depends(get_user_from_jwt_payload),
) -> list[Right]:
    """
    ユーザーの権限を取得する
    """
    return me.role.rights
