"""adding more columns to posts table

Revision ID: 755a19775af8
Revises: 169e50a275e3
Create Date: 2026-05-14 02:25:21.950586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '755a19775af8'
down_revision: Union[str, Sequence[str], None] = '169e50a275e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean, nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() :
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
