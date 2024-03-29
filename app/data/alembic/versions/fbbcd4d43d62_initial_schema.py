"""Initial Schema

Revision ID: fbbcd4d43d62
Revises: 
Create Date: 2024-01-24 21:03:46.299608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbbcd4d43d62'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('announcer', 'broker', 'sysAdmin', name='userrole'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('creci_number', sa.Numeric(), nullable=True),
    sa.Column('document_number', sa.String(length=14), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('creci_number'),
    sa.UniqueConstraint('document_number'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    op.create_table('property_ads',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('neighboorhood', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('listing_purpose', sa.Enum('rental', 'purchase', 'both', name='listingpurpose'), nullable=False),
    sa.Column('property_type', sa.Enum('house', 'apartment', 'commercial', name='propertytype'), nullable=False),
    sa.Column('uf', sa.String(length=2), nullable=True),
    sa.Column('min_budget', sa.Numeric(precision=20, scale=2), nullable=True),
    sa.Column('max_budget', sa.Numeric(precision=20, scale=2), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('mustHaveItems', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('desiredItems', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('announcer_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['announcer_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('term_acceptances',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('term_version', sa.String(length=20), nullable=False),
    sa.Column('accepted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('device_id', sa.String(length=20), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('term_acceptances')
    op.drop_table('property_ads')
    op.drop_table('users')
    # ### end Alembic commands ###
