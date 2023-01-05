"""Add publishers table

Revision ID: 6beed3ea6834
Revises: e4d99f633839
Create Date: 2022-11-09 23:50:18.132716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6beed3ea6834'
down_revision = 'e4d99f633839'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'publishers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String())
    )

    op.add_column('books', sa.Column('publisher_id', sa.Integer, sa.ForeignKey('publishers.id')))


def downgrade():
    pass
