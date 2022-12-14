from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext

from app.database import get_tenant_db


class CustomContext(BaseContext):
    def __init__(self, db: Session):
        super().__init__()
        self.db = db


def get_custom_context_dependency(
    db: Session = Depends(get_tenant_db),
) -> CustomContext:
    return CustomContext(db=db)


async def get_context(
    custom_context: CustomContext = Depends(get_custom_context_dependency),
):
    return custom_context
