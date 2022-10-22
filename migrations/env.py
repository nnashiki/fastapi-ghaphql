from logging.config import fileConfig
from typing import Sequence, Union

from alembic import context
from alembic.operations import ops
from alembic.script import ScriptDirectory
from sqlalchemy import (Column, Constraint, UniqueConstraint,
                        engine_from_config, pool)

from app.models import BaseModel

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support


target_metadata = BaseModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def include_object(obj, name, type_, reflected, compare_to):
    if obj.info.get("skip_autogen", False):
        return False

    return True


def process_revision_directives(context, revision, directives):
    # extract Migration
    migration_script = directives[0]
    # extract current head revision
    head_revision = ScriptDirectory.from_config(context.config).get_current_head()

    # マイグレーションの rev_id をカスタムルールで上書きする
    if head_revision is None:
        # edge case with first migration
        new_rev_id = 1
    else:
        # default branch with incrementation
        last_rev_id = int(head_revision.lstrip("0"))
        new_rev_id = last_rev_id + 1
    # fill zeros up to 4 digits: 1 -> 0001
    migration_script.rev_id = "{0:04}".format(new_rev_id)

    # upgrade directive を上書きする
    migration_script.upgrade_ops.ops = [order_columns(op) for op in migration_script.upgrade_ops.ops]


def order_columns(op):
    if not isinstance(op, ops.CreateTableOp):
        return op

    # order_columns
    special_names = {"id": -100, "created_at": 1001, "updated_at": 1002}
    cols_by_key = [
        (
            special_names.get(col.key, index) if isinstance(col, Column) else 2000,
            col.copy(),
        )
        for index, col in enumerate(op.columns)
    ]
    columns_or_constraints: Sequence[Union[Column, Constraint]] = [
        col for idx, col in sorted(cols_by_key, key=lambda entry: entry[0])
    ]

    # UniqueConstraint の columns_combination が重複した場合、一つに絞り込む
    uc_columns_combinations = []
    for index, column_or_constraint in enumerate(columns_or_constraints):
        if isinstance(column_or_constraint, UniqueConstraint):
            columns_combination = set([col.name for col in column_or_constraint.columns])
            if columns_combination in uc_columns_combinations:
                del columns_or_constraints[index]
            else:
                uc_columns_combinations.append(columns_combination)

    op.columns = columns_or_constraints
    return op


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # MATERIALIZED VIEW など無視する場合は下記をクラス属性に設定する
        # __table_args__ = {"info": {"skip_autogen": True}}
        include_object=include_object,
        # 型変更を検知する
        compare_type=True,
        process_revision_directives=process_revision_directives,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # MATERIALIZED VIEW など無視する場合は下記をクラス属性に設定する
            # __table_args__ = {"info": {"skip_autogen": True}}
            include_object=include_object,
            # 型変更を検知する
            compare_type=True,
            process_revision_directives=process_revision_directives,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
