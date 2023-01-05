"""Add tags and association table

Revision ID: c3c511797625
Revises: 6beed3ea6834
Create Date: 2022-11-15 22:53:08.779936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3c511797625'
down_revision = '6beed3ea6834'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String())
    )
    op.create_table(
        'books_tags',
        sa.Column('book_id', sa.Integer),
        sa.Column('tag_id', sa.Integer)
    )
    pass


def downgrade():
    pass
