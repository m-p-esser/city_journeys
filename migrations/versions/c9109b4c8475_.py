"""empty message

Revision ID: c9109b4c8475
Revises: 
Create Date: 2024-10-05 14:47:58.020540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9109b4c8475'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('state_id', sa.BigInteger(), nullable=False),
    sa.Column('country_id', sa.BigInteger(), nullable=False),
    sa.Column('latitude', sa.Numeric(precision=10, scale=8), nullable=False),
    sa.Column('longitude', sa.Numeric(precision=11, scale=8), nullable=False),
    sa.Column('wikiDataId', sa.String(length=255), nullable=True),
    sa.Column('population', sa.BigInteger(), nullable=True),
    sa.Column('elevation_in_meter', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###
