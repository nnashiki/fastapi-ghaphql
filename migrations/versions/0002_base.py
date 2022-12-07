"""base

Revision ID: 0002
Revises: 0001
Create Date: 2022-12-07 23:27:53.581951+09:00

"""
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
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_roles")),
        sa.UniqueConstraint("name", name=op.f("uq_roles_name")),
        comment="ロール(1:super, 10:basic plan member, 11:basic plan Admin, 20: premium plan member,  21: premium plan admin 99:停止ユーザー",
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
        "right_role_mappings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("right_id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
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
        "tenant_users",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
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
    # ### end Alembic commands ###

    # 後処理
    post_upgrade()


def downgrade() -> None:
    # 前処理
    pre_downgrade()

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("posts")
    op.drop_table("tenant_users")
    op.drop_table("tenants")
    op.drop_table("right_role_mappings")
    op.drop_table("service_plans")
    op.drop_table("roles")
    op.drop_table("rights")
    # ### end Alembic commands ###

    # 後処理
    post_downgrade()


def pre_upgrade():
    # スキーマ更新前に実行する必要がある処理
    pass


def post_upgrade():
    # スキーマ更新後に実行する必要がある処理
    pass


def pre_downgrade():
    # スキーマ更新前に実行する必要がある処理
    pass


def post_downgrade():
    # スキーマ更新後に実行する必要がある処理
    pass
