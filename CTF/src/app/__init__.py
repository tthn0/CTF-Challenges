from flask import Flask

from .classes.config import Config
from .routes import base, restricted

__all__: list[str] = ["Config", "create_app"]


def create_app() -> Flask:
    app: Flask = Flask(import_name=__name__)
    app.config.from_object(obj=Config)
    app.register_blueprint(blueprint=base)
    app.register_blueprint(blueprint=restricted)
    return app
