"""add content column

Revision ID: 9fe060edcf69
Revises: cb00a9ef9dfa
Create Date: 2021-11-22 11:56:29.040240

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '9fe060edcf69'
down_revision = 'cb00a9ef9dfa'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
