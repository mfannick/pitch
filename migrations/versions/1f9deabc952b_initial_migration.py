"""Initial Migration

Revision ID: 1f9deabc952b
Revises: dbf3106de8c6
Create Date: 2019-09-23 14:17:32.894900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f9deabc952b'
down_revision = 'dbf3106de8c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commentWrite', sa.String(length=1000), nullable=True))
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('timeComment', sa.DateTime(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_pitchId_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_userId_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'userId')
    op.drop_column('comments', 'pitchId')
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('pitchId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_userId_fkey', 'comments', 'users', ['userId'], ['id'])
    op.create_foreign_key('comments_pitchId_fkey', 'comments', 'pitches', ['pitchId'], ['id'])
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'timeComment')
    op.drop_column('comments', 'pitch_id')
    op.drop_column('comments', 'commentWrite')
    # ### end Alembic commands ###
