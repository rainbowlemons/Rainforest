"""First migration

Revision ID: 09bc53f8f71e
Revises: 
Create Date: 2022-09-01 22:41:45.134739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09bc53f8f71e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('author', sa.String()),
    )


def downgrade():
    pass
