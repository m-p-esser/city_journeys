import pathlib
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import find_dotenv, load_dotenv
from src.db import Database
from router import Router

template_dir = pathlib.Path.cwd() / "public"
static_dir = pathlib.Path.cwd() / "assets"

load_dotenv()
env_vars = os.environ

# Start the app
app = Flask(
    import_name=__name__,
    template_folder=template_dir,
    # static_folder=static_dir
)

# Init Database
db = Database(
    host=env_vars["HOST_NAME"],
    port=env_vars["PORT"],
    database=env_vars["DATABASE"],
    user=env_vars["USER_NAME"],
    password=env_vars["PASSWORD"],
)
connection_uri = db.create_connection_uri("MySQL")
app.config.from_mapping(
    {"SQLALCHEMY_DATABASE_URI": connection_uri}
)

# Migrate Database
migrate = Migrate(app, db)

Router.run(app)

if __name__ == "__main__":
    app.debug = True
    app.run()
