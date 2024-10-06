"""empty message

Revision ID: 55c26d593788
Revises: 78afaa9edea7
Create Date: 2024-10-06 16:24:06.180576

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '55c26d593788'
down_revision = '78afaa9edea7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('state_id', mysql.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('country_id', mysql.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('latitude', mysql.DECIMAL(precision=10, scale=8), nullable=True),
    sa.Column('longitude', mysql.DECIMAL(precision=11, scale=8), nullable=True),
    sa.Column('wikiDataId', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('population', mysql.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('elevation_in_meter', mysql.BIGINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
