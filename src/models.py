from sqlalchemy import Column, String, Text, SmallInteger, Integer, BigInteger, Numeric
from app import db

city = db.Table(
    "cities",
    Column("id", BigInteger, primary_key=True, nullable=False),
    Column("name", String(255)),
    Column("state_id", SmallInteger),
    Column("country_id", SmallInteger),
    Column("latitude", Numeric(10, 8)),
    Column("longitude", Numeric(11, 8)),
    Column("wikiDataId", String(255)),
    Column("population", BigInteger),
    Column("elevation_in_meter", BigInteger),
)

countries = db.Table(
    "countries",
    Column("id", SmallInteger, primary_key=True, nullable=False),
    Column("name", String(255)),
    Column("iso3", String(10)),
    Column("iso2", String(10)),
    Column("numeric_code", Integer),
    Column("phone_code", Integer),
    Column("capital", String(255)),
    Column("currency", String(10)),
    Column("currency_name", String(100)),
    Column("currency_symbol", String(10)),
    Column("tld", String(10)),
    Column("native", String(100)),
    Column("region_id", SmallInteger),
    Column("subregion_id", SmallInteger),
    Column("nationality", String(100)),
    Column("timezones", Text),
    Column("latitude", Numeric(10, 8)),
    Column("longitude", Numeric(11, 8)),
    Column("emoji", String(100)),
    Column("emojiU", String(255)),
    Column("wikiDataId", String(255)),
)

regions = db.Table(
    "regions",
    Column("id", SmallInteger, primary_key=True, nullable=False),
    Column("name", String(255)),
    Column("wikiDataId", String(255)),
)

subregions = db.Table(
    "subregions",
    Column("id", SmallInteger, primary_key=True, nullable=False),
    Column("name", String(255)),
    Column("region_id", SmallInteger),
    Column("wikiDataId", String(255)),
)

states = db.Table(
    "states",
    Column("id", SmallInteger, primary_key=True, nullable=False),
    Column("name", String(255)),
    Column("country_id", SmallInteger),
    Column("state_code", String(10)),
    Column("type", String(100)),
    Column("longitude", Numeric(11, 8)),
)
