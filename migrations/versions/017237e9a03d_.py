"""empty message

Revision ID: 017237e9a03d
Revises: af1b8b0fa3ab
Create Date: 2021-04-14 15:59:33.272787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '017237e9a03d'
down_revision = 'af1b8b0fa3ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Announcement', sa.Column('subject', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Announcement', 'subject')
    # ### end Alembic commands ###
