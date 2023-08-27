"""Create Events table

Revision ID: d7a77e0a78b0
Revises: 
Create Date: 2023-08-20 00:41:52.661777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel as sm


# revision identifiers, used by Alembic.
revision: str = 'd7a77e0a78b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

#Changes that need to be made to the database need to be put in the upgrade function 
def upgrade() -> None:
    op.create_table('events',sa.Column('title', sm.sql.sqltypes.AutoString(), nullable=False), 
                             sa.Column('description', sm.sql.sqltypes.AutoString(), nullable=False)
                    )


#Changes that need to be removed form the database need to be put in the downgrade function (rollback)
def downgrade() -> None:
    op.drop_table('events')
