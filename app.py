from flask import Flask
from src.framework.router import Router
import pathlib

template_dir = pathlib.Path.cwd() / 'public'
static_dir = pathlib.Path.cwd() / 'assets'

# Start the app
app = Flask(
    import_name=__name__,
    template_folder=template_dir,
    # static_folder=static_dir
    )

Router.run(app)

if __name__ == '__main__':
    app.debug = True
    app.run()