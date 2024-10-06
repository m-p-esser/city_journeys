import pathlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.db import db_client
from src.router import Router

template_dir = pathlib.Path.cwd() / "public"
static_dir = pathlib.Path.cwd() / "static"

# Start the app
app = Flask(
    import_name=__name__,
    template_folder=template_dir,
    static_folder=static_dir
)

# Init Database
sql = f"CREATE DATABASE IF NOT EXISTS {db_client.config.DB_NAME}"
db_client.create_query(sql)

connection_uri = db_client.create_connection_uri("MySQL")
app.config.from_mapping({"SQLALCHEMY_DATABASE_URI": connection_uri})
db = SQLAlchemy(app)

# Migrate Database
migrate = Migrate(app, db)

# Start App on Landing page
Router.run(app)

# forces table creation
from src import models


if __name__ == "__main__":
    app.debug = True
    app.run()
