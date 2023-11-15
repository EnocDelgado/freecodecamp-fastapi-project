"""add content column to posts table

Revision ID: 63301c10e8cf
Revises: 929686636d67
Create Date: 2023-11-14 21:23:24.370299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63301c10e8cf'
down_revision: Union[str, None] = '929686636d67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass