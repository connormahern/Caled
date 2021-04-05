"""empty message

Revision ID: c359384bb2cc
Revises: 58cffccd4257
Create Date: 2021-03-29 21:00:13.762647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c359384bb2cc'
down_revision = '58cffccd4257'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    

    op.create_table('User',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"User_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('userType', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('hasAccess', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='User_pkey'),
    sa.UniqueConstraint('email', name='User_email_key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User')
    op.drop_table('Instructor')
    op.drop_table('Student')
    op.drop_table('Admin')
    op.drop_table('Course')
    op.drop_table('StudentCourses')
    op.drop_table('Message')
    # ### end Alembic commands ###
