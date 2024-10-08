"""empty message

Revision ID: 78c05acad026
Revises: 6c2a65e54bf6
Create Date: 2024-10-05 21:02:36.399232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78c05acad026'
down_revision = '6c2a65e54bf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('regions',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('wikiDataId', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('regions')
    # ### end Alembic commands ###
