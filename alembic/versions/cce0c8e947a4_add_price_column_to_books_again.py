"""Add price column to books again

Revision ID: cce0c8e947a4
Revises: 5d5e2dd683e3
Create Date: 2022-11-28 00:28:55.000888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cce0c8e947a4'
down_revision = '5d5e2dd683e3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('books', sa.Column('price', sa.Float))


def downgrade():
    pass
