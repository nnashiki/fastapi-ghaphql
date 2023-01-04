from sqlalchemy.orm import joinedload

from app import models
from app_tests.util import create_tenant_and_users


class TestUsers:
    def test_create(self, session):
        tenant, tenant_user = create_tenant_and_users(session)
        assert tenant_user.name == "沖田総司"
        assert tenant.tenant_users[0].id == tenant_user.id

    def test_tenantを削除するとuserも削除される(self, session):  # noqa
        tenant, tenant_user = create_tenant_and_users(session)
        session.delete(tenant)
        session.commit()
        assert session.query(models.TenantUser).count() == 0


class TestPostLike:
    def test_create(self, session):
        tenant, tenant_user = create_tenant_and_users(session)

        post = models.Post(title="title", detail="detail", tenant_id=tenant.id, posted_by_id=tenant_user.id)
        session.add(post)
        session.flush()

        post_like = models.PostLike(post_id=post.id, tenant_user_id=tenant_user.id)
        session.add(post_like)
        session.flush()

        post_comment = models.PostComment(comment="comment", post_id=post.id, tenant_user_id=tenant_user.id)
        session.add(post_comment)
        session.commit()

        query = session.query(models.Post).options(joinedload(models.Post.post_likes))
        print(query.statement.compile(compile_kwargs={"literal_binds": True}))
        print(query.one())
