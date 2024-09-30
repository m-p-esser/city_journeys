from src.routes.HomeRouter import home_router


class Router:

    def run(app):

        app.register_blueprint(home_router, url_prefix="/")
