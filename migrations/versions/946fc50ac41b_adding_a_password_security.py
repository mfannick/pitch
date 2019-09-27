"""adding a password security

Revision ID: 946fc50ac41b
Revises: fed1f86d4f91
Create Date: 2019-09-20 12:50:58.946411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '946fc50ac41b'
down_revision = 'fed1f86d4f91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_foreign_key(None, 'users', 'pitches', ['pitch_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'pitch_id')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    op.drop_table('pitches')
    # ### end Alembic commands ###
