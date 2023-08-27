"""add phone number to events tables

Revision ID: db96dbde20e9
Revises: d7a77e0a78b0
Create Date: 2023-08-20 20:47:04.668433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel as sm


# revision identifiers, used by Alembic.
revision: str = 'db96dbde20e9'
down_revision: Union[str, None] = 'd7a77e0a78b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('events', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('events', 'phone_number')
    pass
