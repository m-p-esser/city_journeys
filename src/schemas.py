from pydantic import BaseModel

class City(BaseModel):
    id: int
    name: str | None = None
    state_id: int | None = None
    country_id: int | None = None
    latitude: float | None = None
    longitude: float | None = None
    wikiDataId: str | None = None
    population: int | None = None
    elevation_in_meter: int | None = None

    class Config:
        from_attributes = True

class Country(BaseModel):
    id: int
    name: str | None = None
    iso3: str | None = None
    iso2: str | None = None
    numeric_code: int | None = None
    phone_code: int | None = None
    capital: str | None = None
    currency: str | None = None
    currency_name: str | None = None
    currency_symbol: str | None = None
    tld: str | None = None
    native: str | None = None
    region_id: int | None = None
    subregion_id: int | None = None
    nationality: str | None = None
    timezones: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    emoji: str | None = None
    emojiU: str | None = None
    wikiDataId: str | None = None

    class Config:
        from_attributes = True