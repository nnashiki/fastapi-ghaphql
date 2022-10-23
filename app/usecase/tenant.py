from app.database import session
from app.models import Tenant


def read_my_tenant() -> Tenant:
    tenant = session().query(Tenant).filter(Tenant.id == "de583d0a-e132-4c61-9b08-64685112046c").one()
    return tenant


def create_tenant(name: str) -> Tenant:
    tenant = Tenant(name=name)
    _session = session()
    _session.add(tenant)
    _session.commit()
    _session = session()
    tenant = _session.query(Tenant).filter(Tenant.name == name).one()
    return tenant
