"""create_users_table

Revision ID: 82dffe4f2ba5
Revises: 
Create Date: 2026-05-01 17:48:38.642371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82dffe4f2ba5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
            nullable=False
        ),

        sa.Column(
            "name",
            sa.String(length=50),
            nullable=True
        ),

        sa.Column(
            "email",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "phone",
            sa.String(length=20),
            nullable=True
        ),

        sa.Column(
            "address",
            sa.Text(),
            nullable=True
        ),

        sa.Column(
            "password",
            sa.Text(),
            nullable=False
        ),

        sa.Column(
            "is_active",
            sa.Boolean(),
            default=True
        ),

        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("NOW()"),
            nullable=False
        ),

        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True
        )
    )

    op.create_index(
        op.f("ix_users_id"),
        "users",
        ["id"],
        unique=False
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_users_id"),
        table_name="users"
    )

    op.drop_table("users")
