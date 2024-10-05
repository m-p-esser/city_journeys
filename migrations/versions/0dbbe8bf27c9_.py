"""empty message

Revision ID: 0dbbe8bf27c9
Revises: 27cd35aa97de
Create Date: 2024-10-05 20:52:54.183585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dbbe8bf27c9'
down_revision = '27cd35aa97de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countries',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('iso3', sa.String(length=10), nullable=True),
    sa.Column('iso2', sa.String(length=10), nullable=True),
    sa.Column('numeric_code', sa.Integer(), nullable=True),
    sa.Column('phone_code', sa.Integer(), nullable=True),
    sa.Column('capital', sa.String(length=255), nullable=True),
    sa.Column('currency', sa.String(length=10), nullable=True),
    sa.Column('currency_name', sa.String(length=100), nullable=True),
    sa.Column('currency_symbol', sa.String(length=10), nullable=True),
    sa.Column('tld', sa.String(length=10), nullable=True),
    sa.Column('native', sa.String(length=100), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.Column('subregion_id', sa.Integer(), nullable=True),
    sa.Column('nationality', sa.String(length=100), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=10, scale=8), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=11, scale=8), nullable=True),
    sa.Column('emoji', sa.String(length=100), nullable=True),
    sa.Column('emojiU', sa.String(length=255), nullable=True),
    sa.Column('wikiDataId', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('countries')
    # ### end Alembic commands ###
