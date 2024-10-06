from flask import render_template
import boto3
from config.config import static_file_space_config, db_config
from src.db import DatabaseClient


def construct_cnd_url(city_name: str, country_name: str):
    endpoint_url = static_file_space_config.SPACES_ENDPOINT_URL
    region_name = static_file_space_config.SPACES_REGION_NAME
    aws_access_key_id = static_file_space_config.SPACES_AWS_ACCESS_KEY_ID
    aws_secret_access_key = static_file_space_config.SPACES_AWS_SECRET_ACCESS_KEY

    session = boto3.session.Session()
    client = session.client(
        "s3",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    response = client.list_objects(
        Bucket="travel-app-prod-images", Prefix=f"{city_name}_{country_name}"
    )
    objects = response.get("Contents")
    if isinstance(objects, list):
        object_key = objects[0].get("Key")  # Take first image

        cdn_domain = (
            f"https://travel-app-prod-images.{region_name}.cdn.digitaloceanspaces.com"
        )
        return f"{cdn_domain}/{object_key}"


class HomeController:

    def view_cities():
        db_client = DatabaseClient()
        sql = """
        SELECT 
            cities.id,
            cities.name AS city_name,
            cities.population AS city_population,
            countries.name AS country_name,
            countries.emoji AS country_emoji 
        FROM db_prod.cities AS cities
        LEFT JOIN db_prod.countries AS countries
        ON cities.country_id = countries.id
        WHERE cities.population > 100000
        ORDER BY cities.population DESC
        LIMIT 20
        """
        cities = db_client.read_query(sql)
        for c in cities:
            c["cdn_url"] = construct_cnd_url(c["city_name"], c["country_name"])

        return render_template("index.html", cities=cities)
