from fastapi import FastAPI
from fastapi import HTTPException
import schemas
from db import db_client

app = FastAPI()


@app.get("/cities", response_model=list[schemas.City])
def get_users():
    cities = db_client.get_cities()
    return cities


@app.get("/cities/{city_id}", response_model=schemas.City)
def get_user(city_id: int):
    city = db_client.get_city(city_id=city_id)
    if city is None:
        raise HTTPException(
            status_code=404, detail=f"City with ID '{city_id}' not found"
        )
    return city


@app.get("/countries", response_model=list[schemas.Country])
def get_users():
    countries = db_client.get_countries()
    return countries


@app.get("/countries/{country_id}", response_model=schemas.City)
def get_user(country_id: int):
    country = db_client.get_coutry(country_id=country_id)
    if country is None:
        raise HTTPException(
            status_code=404, detail=f"Country with ID '{country_id}' not found"
        )
    return country
