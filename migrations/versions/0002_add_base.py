"""add_base

Revision ID: 0002
Revises: 0001
Create Date: 2022-12-28 11:05:28.936820+09:00

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 前処理
    pre_upgrade()

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "rights",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rights")),
        sa.UniqueConstraint("name", name=op.f("uq_rights_name")),
        comment="権限",
    )
    op.create_table(
        "service_plans",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_service_plans")),
        sa.UniqueConstraint("name", name=op.f("uq_service_plans_name")),
        comment="サービスプラン",
    )
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("service_plan_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["service_plan_id"],
            ["service_plans.id"],
            name=op.f("fk_roles_service_plan_id_service_plans"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_roles")),
        sa.UniqueConstraint("name", name=op.f("uq_roles_name")),
        comment="ロール(1:super, 10:basic plan member, 11:basic plan Admin, 20: premium plan member,  21: premium plan admin 99:停止ユーザー",
    )
    op.create_table(
        "tenants",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("service_plan_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["service_plan_id"],
            ["service_plans.id"],
            name=op.f("fk_tenants_service_plan_id_service_plans"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tenants")),
        sa.UniqueConstraint("name", name=op.f("uq_tenants_name")),
    )
    op.create_table(
        "right_role_mappings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.Column("right_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["right_id"],
            ["rights.id"],
            name=op.f("fk_right_role_mappings_right_id_rights"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
            name=op.f("fk_right_role_mappings_role_id_roles"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_right_role_mappings")),
        sa.UniqueConstraint("right_id", "role_id", name=op.f("uq_right_role_mappings_right_id")),
        comment="権限ロールマッピング",
    )
    op.create_table(
        "tenant_users",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("idaas_id", sa.String(length=36), nullable=False),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
            name=op.f("fk_tenant_users_role_id_roles"),
        ),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenants.id"],
            name=op.f("fk_tenant_users_tenant_id_tenants"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tenant_users")),
        sa.UniqueConstraint("name", "tenant_id", name=op.f("uq_tenant_users_name")),
        comment="ユーザー",
    )
    op.create_table(
        "posts",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("detail", sa.String(length=255), nullable=False),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("posted_by_id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["posted_by_id"],
            ["tenant_users.id"],
            name=op.f("fk_posts_posted_by_id_tenant_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenants.id"],
            name=op.f("fk_posts_tenant_id_tenants"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_posts")),
        sa.UniqueConstraint("title", "tenant_id", name=op.f("uq_posts_title")),
        comment="投稿",
    )
    op.create_table(
        "post_comments",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("post_id", sa.BigInteger(), nullable=False),
        sa.Column("tenant_user_id", sa.String(length=36), nullable=False),
        sa.Column("comment", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
            name=op.f("fk_post_comments_post_id_posts"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["tenant_user_id"],
            ["tenant_users.id"],
            name=op.f("fk_post_comments_tenant_user_id_tenant_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_post_comments")),
        sa.UniqueConstraint("post_id", "tenant_user_id", name=op.f("uq_post_comments_post_id")),
        comment="投稿コメント",
    )
    op.create_table(
        "post_likes",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("post_id", sa.BigInteger(), nullable=False),
        sa.Column("tenant_user_id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
            name=op.f("fk_post_likes_post_id_posts"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["tenant_user_id"],
            ["tenant_users.id"],
            name=op.f("fk_post_likes_tenant_user_id_tenant_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_post_likes")),
        sa.UniqueConstraint("post_id", "tenant_user_id", name=op.f("uq_post_likes_post_id")),
        comment="投稿いいね",
    )
    # ### end Alembic commands ###

    # 後処理
    post_upgrade()


def downgrade() -> None:
    # 前処理
    pre_downgrade()

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("post_likes")
    op.drop_table("post_comments")
    op.drop_table("posts")
    op.drop_table("tenant_users")
    op.drop_table("right_role_mappings")
    op.drop_table("tenants")
    op.drop_table("roles")
    op.drop_table("service_plans")
    op.drop_table("rights")
    # ### end Alembic commands ###

    # 後処理
    post_downgrade()


def pre_upgrade():
    # スキーマ更新前に実行する必要がある処理
    pass


def post_upgrade():
    # スキーマ更新後に実行する必要がある処理
    service_plans = sa.table(
        "service_plans",
        sa.column("id", sa.Integer),
        sa.column("name", sa.String(length=255)),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )
    op.bulk_insert(
        service_plans,
        [
            {"id": 1, "name": "free", "created_at": datetime.now(), "updated_at": datetime.now()},
            {"id": 2, "name": "basic", "created_at": datetime.now(), "updated_at": datetime.now()},
            {"id": 99, "name": "suspended", "created_at": datetime.now(), "updated_at": datetime.now()},
            {"id": 777, "name": "super", "created_at": datetime.now(), "updated_at": datetime.now()},
        ],
    )
    rights = sa.table(
        "rights",
        sa.column("id", sa.Integer),
        sa.column("name", sa.String(length=255)),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )
    # tenant に紐づく権限
    create_tenant_right_id = 1
    read_tenant_right_id = 2
    update_tenant_right_id = 3
    delete_tenant_right_id = 4
    # tenant_user に紐づく権限
    create_tenant_user_right_id = 5
    read_tenant_user_right_id = 6
    update_tenant_user_right_id = 7
    delete_tenant_user_right_id = 8
    rights_data = [
        {"id": create_tenant_right_id, "name": "create.tenant"},
        {"id": read_tenant_right_id, "name": "read.tenant"},
        {"id": update_tenant_right_id, "name": "update.tenant"},
        {"id": delete_tenant_right_id, "name": "delete.tenant"},
        {"id": create_tenant_user_right_id, "name": "create.tenant_user"},
        {"id": read_tenant_user_right_id, "name": "read.tenant_user"},
        {"id": update_tenant_user_right_id, "name": "update.tenant_user"},
        {"id": delete_tenant_user_right_id, "name": "delete.tenant_user"},
    ]
    op.bulk_insert(
        rights,
        [dict({"created_at": datetime.now(), "updated_at": datetime.now()}, **row) for row in rights_data],
    )
    roles = sa.table(
        "roles",
        sa.column("id", sa.Integer),
        sa.column("name", sa.String(length=255)),
        sa.Column("service_plan_id", sa.Integer, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )
    free_tenant_member_role_id = 1
    free_tenant_admin_role_id = 2
    basic_tenant_member_role_id = 3
    basic_tenant_admin_role_id = 4
    super_user_role_id = 777
    roles_data = [
        {"id": free_tenant_member_role_id, "name": "free_tenant_member", "service_plan_id": 1},
        {"id": free_tenant_admin_role_id, "name": "free_tenant_admin", "service_plan_id": 1},
        {"id": basic_tenant_member_role_id, "name": "basic_tenant_member", "service_plan_id": 2},
        {"id": basic_tenant_admin_role_id, "name": "basic_tenant_admin", "service_plan_id": 2},
        {"id": 99, "name": "suspended_user", "service_plan_id": 99},
        {"id": super_user_role_id, "name": "super_user", "service_plan_id": 777},
    ]
    op.bulk_insert(
        roles,
        [dict({"created_at": datetime.now(), "updated_at": datetime.now()}, **row) for row in roles_data],
    )
    right_role_mappings = sa.table(
        "right_role_mappings",
        sa.column("id", sa.Integer),
        sa.column("role_id", sa.Integer),
        sa.column("right_id", sa.Integer),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )
    right_role_mappings_data = [
        {"id": 1, "role_id": super_user_role_id, "right_id": create_tenant_right_id},
        {"id": 2, "role_id": super_user_role_id, "right_id": read_tenant_right_id},
        {"id": 3, "role_id": super_user_role_id, "right_id": update_tenant_right_id},
        {"id": 4, "role_id": super_user_role_id, "right_id": delete_tenant_right_id},
        {"id": 5, "role_id": free_tenant_member_role_id, "right_id": read_tenant_user_right_id},
        {"id": 6, "role_id": free_tenant_admin_role_id, "right_id": create_tenant_user_right_id},
        {"id": 7, "role_id": free_tenant_admin_role_id, "right_id": read_tenant_user_right_id},
        {"id": 8, "role_id": free_tenant_admin_role_id, "right_id": update_tenant_user_right_id},
        {"id": 9, "role_id": free_tenant_admin_role_id, "right_id": delete_tenant_user_right_id},
        {"id": 10, "role_id": basic_tenant_member_role_id, "right_id": read_tenant_user_right_id},
        {"id": 11, "role_id": basic_tenant_admin_role_id, "right_id": create_tenant_user_right_id},
        {"id": 12, "role_id": basic_tenant_admin_role_id, "right_id": read_tenant_user_right_id},
        {"id": 13, "role_id": basic_tenant_admin_role_id, "right_id": update_tenant_user_right_id},
        {"id": 14, "role_id": basic_tenant_admin_role_id, "right_id": delete_tenant_user_right_id},
        {"id": 15, "role_id": super_user_role_id, "right_id": read_tenant_user_right_id},
        {"id": 16, "role_id": super_user_role_id, "right_id": create_tenant_user_right_id},
        {"id": 17, "role_id": super_user_role_id, "right_id": update_tenant_user_right_id},
        {"id": 18, "role_id": super_user_role_id, "right_id": delete_tenant_user_right_id},
    ]
    op.bulk_insert(
        right_role_mappings,
        [
            dict({"created_at": datetime.now(), "updated_at": datetime.now()}, **row)
            for row in right_role_mappings_data
        ],
    )


def pre_downgrade():
    # スキーマ更新前に実行する必要がある処理
    op.execute("DELETE FROM right_role_mappings")
    op.execute("DELETE FROM roles")
    op.execute("DELETE FROM rights")
    op.execute("DELETE FROM service_plans")


def post_downgrade():
    # スキーマ更新後に実行する必要がある処理
    pass
