"""User

Revision ID: c8aa4596a63b
Revises: 
Create Date: 2024-01-03 12:33:20.663142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8aa4596a63b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users_detail",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("user_name", sa.String(100), nullable=False),
        sa.Column("password", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("users_detail")
