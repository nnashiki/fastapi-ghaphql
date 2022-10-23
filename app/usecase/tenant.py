from app.database import session
from app.models import Tenant


def read_my_tenant() -> Tenant:
    tenant = session().query(Tenant).filter(Tenant.id == "de583d0a-e132-4c61-9b08-64685112046c").one()
    return tenant
