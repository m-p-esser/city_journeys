import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# metadata = sa.MetaData()

city = db.Table(
    'cities',
    sa.Column('id', sa.BigInteger, primary_key=True, nullable=False),
    sa.Column('name', sa.String(255)),
    sa.Column('state_id', sa.SmallInteger),
    sa.Column('country_id', sa.SmallInteger),
    sa.Column('latitude', sa.Numeric(10,8)),
    sa.Column('longitude', sa.Numeric(11,8)),
    sa.Column('wikiDataId', sa.String(255)),
    sa.Column('population', sa.BigInteger),
    sa.Column('elevation_in_meter', sa.BigInteger)
)

countries = db.Table(
    'countries',
    sa.Column('id', sa.SmallInteger, primary_key=True, nullable=False),
    sa.Column('name', sa.String(255)),
    sa.Column('iso3', sa.String(10)),
    sa.Column('iso2', sa.String(10)),
    sa.Column('numeric_code', sa.Integer),
    sa.Column('phone_code', sa.Integer),
    sa.Column('capital', sa.String(255)),
    sa.Column('currency', sa.String(10)),
    sa.Column('currency_name', sa.String(100)),
    sa.Column('currency_symbol', sa.String(10)),
    sa.Column('tld', sa.String(10)),
    sa.Column('native', sa.String(100)),
    sa.Column('region_id', sa.SmallInteger),
    sa.Column('subregion_id', sa.SmallInteger),
    sa.Column('nationality', sa.String(100)),
    sa.Column('timezones', sa.Text),
    sa.Column('latitude', sa.Numeric(10,8)),
    sa.Column('longitude', sa.Numeric(11,8)),
    sa.Column('emoji', sa.String(100)),
    sa.Column('emojiU', sa.String(255)),
    sa.Column('wikiDataId', sa.String(255)),
)

regions = db.Table(
    'regions',
    sa.Column('id', sa.SmallInteger, primary_key=True, nullable=False),
    sa.Column('name', sa.String(255)),
    sa.Column('wikiDataId', sa.String(255)),
)

subregions = db.Table(
    'subregions',
    sa.Column('id', sa.SmallInteger, primary_key=True, nullable=False),
    sa.Column('name', sa.String(255)),
    sa.Column('region_id', sa.SmallInteger),
    sa.Column('wikiDataId', sa.String(255)),
)

states = db.Table(
    'states',
    sa.Column('id', sa.SmallInteger, primary_key=True, nullable=False),
    sa.Column('name', sa.String(255)),
    sa.Column('country_id', sa.SmallInteger),
    sa.Column('state_code', sa.String(10)),
    sa.Column('type', sa.String(100)),
    sa.Column('longitude', sa.Numeric(11,8)),
)