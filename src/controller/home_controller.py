from flask import render_template
from config.config import static_file_space_config, db_config
from src.db import DatabaseClient


class HomeController:

    # def construct_cnd_url(image_path):
    #     endpoint_url = static_file_space_config.SPACES_ENDPOINT_URL
    #     region_name = static_file_space_config.SPACES_REGION_NAME
    #     aws_access_key_id = static_file_space_config.SPACES_AWS_ACCESS_KEY_ID
    #     aws_secret_access_key = static_file_space_config.SPACES_AWS_SECRET_ACCESS_KEY

    #     cdn_domain = f"https://travel-app-prod-images.{region_name}.cdn.digitaloceanspaces.com"
    #     return f"{cdn_domain}/{image_path}"

    def view_cities():
        db_client = DatabaseClient()
        sql = """
        SELECT 
            cities.id,
            cities.name AS city_name,
            countries.name AS country_name,
            countries.emoji AS country_emoji 
        FROM db_prod.cities AS cities
        LEFT JOIN db_prod.countries AS countries
        ON cities.country_id = countries.id
        LIMIT 50
        """
        cities = db_client.read_query(sql)
        return render_template("index.html", cities=cities)
