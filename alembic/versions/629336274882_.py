"""empty message

Revision ID: 629336274882
Revises: 
Create Date: 2024-07-23 20:13:38.384282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '629336274882'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authsession',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('session_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('expiration', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('authsession', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_authsession_session_id'), ['session_id'], unique=True)
        batch_op.create_index(batch_op.f('ix_authsession_user_id'), ['user_id'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password_hash', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    with op.batch_alter_table('ratings', schema=None) as batch_op:
        batch_op.drop_index('id')

    op.drop_table('ratings')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ratings',
    sa.Column('id', mysql.BIGINT(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('origin', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('rating', mysql.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('ratings', schema=None) as batch_op:
        batch_op.create_index('id', ['id'], unique=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    with op.batch_alter_table('authsession', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_authsession_user_id'))
        batch_op.drop_index(batch_op.f('ix_authsession_session_id'))

    op.drop_table('authsession')
    # ### end Alembic commands ###
