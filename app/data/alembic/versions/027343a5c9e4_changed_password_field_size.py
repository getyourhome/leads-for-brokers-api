"""Changed password field size

Revision ID: 027343a5c9e4
Revises: fbbcd4d43d62
Create Date: 2024-01-25 20:00:53.470851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "027343a5c9e4"
down_revision: Union[str, None] = "fbbcd4d43d62"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "password",
        existing_type=sa.VARCHAR(length=64),
        type_=sa.String(length=255),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "password",
        existing_type=sa.String(length=255),
        type_=sa.VARCHAR(length=64),
        existing_nullable=False,
    )
