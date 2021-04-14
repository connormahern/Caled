"""empty message

Revision ID: 336d133fed46
Revises: b31e7dc3f1d8
Create Date: 2021-04-10 17:43:16.778404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '336d133fed46'
down_revision = 'b31e7dc3f1d8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('StudentCourses',
    sa.Column('courseId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('studentId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['courseId'], ['Course.id'], name='StudentCourses_courseId_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['studentId'], ['Student.id'], name='StudentCourses_studentId_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('courseId', 'studentId', name='StudentCourses_pkey')
    )
    op.create_table('Instructor',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['User.id'], name='Instructor_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Instructor_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('UserOrganizations',
    sa.Column('organizationId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['organizationId'], ['Organization.id'], name='UserOrganizations_organizationId_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userId'], ['User.id'], name='UserOrganizations_userId_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('organizationId', 'userId', name='UserOrganizations_pkey')
    )
    op.create_table('User',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"User_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('userType', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('hasAccess', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='User_pkey'),
    sa.UniqueConstraint('email', name='User_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Admin',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['User.id'], name='Admin_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Admin_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Student',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['User.id'], name='Student_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Student_pkey')
    )
    op.create_table('Organization',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Organization_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('adminId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['adminId'], ['Admin.id'], name='Organization_adminId_fkey'),
    sa.PrimaryKeyConstraint('id', name='Organization_pkey')
    )
    op.create_table('Message',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Message_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('message', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('senderId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('recipientId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('dateTime', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('isRead', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['recipientId'], ['User.id'], name='Message_recipientId_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['senderId'], ['User.id'], name='Message_senderId_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='Message_pkey')
    )
    op.create_table('Course',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Course_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('instructorId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=10000), autoincrement=False, nullable=True),
    sa.Column('semester', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('organization', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['instructorId'], ['Instructor.id'], name='Course_instructorId_fkey'),
    sa.PrimaryKeyConstraint('id', name='Course_pkey')
    )


def downgrade():
    pass
