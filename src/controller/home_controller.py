from flask import render_template
import boto3
import requests
from config.config import static_file_space_config, db_config
from src.db import DatabaseClient


def construct_cnd_url(client, city_name: str, country_name: str, region_name: str):

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

        response = requests.get(url="http://127.0.0.1:8000/cities")
        response.raise_for_status()
        cities = response.json()

        response = requests.get(url="http://127.0.0.1:8000/countries")
        response.raise_for_status()
        countries = response.json()

        cities_expanded = []

        for ct in cities:
            country_id = ct["country_id"]
            country = [cn for cn in countries if cn["id"] == country_id][0]
            country_name, country_emoji = country["name"], country["emoji"]
            ct["country_name"] = country_name
            ct["country_emoji"] = country_emoji
            ct["city_name"] = ct.pop("name")
            ct["cdn_url"] = construct_cnd_url(
                client=client,
                city_name=ct["city_name"],
                country_name=ct["country_name"],
                region_name=region_name
            )  # This step takes forever
            cities_expanded.append(ct)

        return render_template("index.html", cities=cities_expanded)
