"""create posts table

Revision ID: acbd5aa25c70
Revises: 
Create Date: 2026-05-13 12:17:10.788413

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acbd5aa25c70'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('title', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('posts')

    pass
    
