from app import models


def create_tenant_and_users(session):
    plan = models.ServicePlan(name="free")
    session.add(plan)
    session.commit()

    tenant = models.Tenant(name="新撰組", service_plan_id=plan.id)
    session.add(tenant)
    session.commit()

    team = models.Team(name="一番隊", tenant_id=tenant.id)
    session.add(team)
    session.commit()

    user = models.User(tenant_id=tenant.id, team_id=team.id, name="沖田総司")
    session.add(user)
    session.commit()
    return user.tenant, user.team, user
