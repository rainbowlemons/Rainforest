"""Add price column to books

Revision ID: 5d5e2dd683e3
Revises: c3c511797625
Create Date: 2022-11-28 00:23:25.490225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5e2dd683e3'
down_revision = 'c3c511797625'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('books', sa.Column('price', sa.Float))


def downgrade():
    pass
