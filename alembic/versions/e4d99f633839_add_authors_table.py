"""Add authors table

Revision ID: e4d99f633839
Revises: 09bc53f8f71e
Create Date: 2022-09-02 00:29:41.613098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4d99f633839'
down_revision = '09bc53f8f71e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String())
    )

    op.add_column('books', sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.id')))

    op.execute('DELETE FROM books;')
    op.drop_column('books', 'author')

def downgrade():
    pass
