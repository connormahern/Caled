"""new migration

Revision ID: c5f4c43ee013
Revises: c359384bb2cc
Create Date: 2021-03-29 21:01:50.457879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5f4c43ee013'
down_revision = 'c359384bb2cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('userType', sa.String(length=100), nullable=True),
    sa.Column('hasAccess', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Message',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('message', sa.String(length=100), nullable=False),
    sa.Column('senderId', sa.Integer(), nullable=True),
    sa.Column('recipientId', sa.Integer(), nullable=True),
    sa.Column('dateTime', sa.DateTime(), nullable=False),
    sa.Column('isRead', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['recipientId'], ['User.id'], ondelete='set null'),
    sa.ForeignKeyConstraint(['senderId'], ['User.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Message')
    op.drop_table('User')
    # ### end Alembic commands ###