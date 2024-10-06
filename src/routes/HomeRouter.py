from flask import Blueprint
from src.controller.home_controller import HomeController

home_router = Blueprint(name="home_controller", import_name=__name__)
home_router.route("/", methods=["GET"])(HomeController.view_cities)
