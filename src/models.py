import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# metadata = sa.MetaData()

city = db.Table(
    'cities',
    # metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, nullable=False),
    sa.Column('name', sa.String(255), nullable=False),
    sa.Column('state_id', sa.BigInteger, nullable=False),
    sa.Column('country_id', sa.BigInteger, nullable=False),
    sa.Column('latitude', sa.Numeric(10,8), nullable=False),
    sa.Column('longitude', sa.Numeric(11,8), nullable=False),
    sa.Column('wikiDataId', sa.String(255)),
    sa.Column('population', sa.BigInteger),
    sa.Column('elevation_in_meter', sa.BigInteger)
)

