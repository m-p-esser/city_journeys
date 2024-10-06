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