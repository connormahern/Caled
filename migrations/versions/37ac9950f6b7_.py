"""empty message

Revision ID: 37ac9950f6b7
Revises: 9d4408a159f1
Create Date: 2021-04-10 17:10:52.028177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37ac9950f6b7'
down_revision = '9d4408a159f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('adminId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['adminId'], ['Admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('UserOrganizations',
    sa.Column('organizationId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organizationId'], ['Organization.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['userId'], ['User.id'], ondelete='set null'),
    sa.PrimaryKeyConstraint('organizationId', 'userId')
    )
    op.drop_column('Course', 'semester')
    op.drop_column('Course', 'organization')
    op.drop_column('Course', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Course', sa.Column('description', sa.VARCHAR(length=10000), autoincrement=False, nullable=True))
    op.add_column('Course', sa.Column('organization', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('Course', sa.Column('semester', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_table('UserOrganizations')
    op.drop_table('Organization')
    # ### end Alembic commands ###
