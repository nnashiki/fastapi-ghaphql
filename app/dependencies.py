from typing import Any

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Right, TenantUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_jwt_payload(token: str = Depends(oauth2_scheme)) -> dict[str, Any]:
    """
    JWTトークンからpayloadを取得する
    """
    payload = jwt.decode(
        token,
        "private_key",
        algorithms=["HS256"],
    )
    return payload


def get_user_from_jwt_payload(
    payload: dict[str, Any] = Depends(get_jwt_payload),
    session: Session = Depends(get_db),
) -> TenantUser:
    """
    JWTトークン payload からユーザーを取得する
    """

    user = session.query(TenantUser).filter(TenantUser.idaas_id == payload["idaas_id"]).one()
    # ここに様々なバリデーションが入る
    return user


def get_my_rights(
    me: TenantUser = Depends(get_user_from_jwt_payload),
) -> list[Right]:
    """
    ユーザーの権限を取得する
    """
    return me.role.rights
