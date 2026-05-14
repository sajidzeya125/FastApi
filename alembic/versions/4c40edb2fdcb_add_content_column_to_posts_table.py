"""add content column to posts table

Revision ID: 4c40edb2fdcb
Revises: acbd5aa25c70
Create Date: 2026-05-13 13:36:33.003832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c40edb2fdcb'
down_revision: Union[str, Sequence[str], None] = 'acbd5aa25c70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
