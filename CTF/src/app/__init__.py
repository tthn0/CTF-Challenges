from flask import Flask

from .classes import Config, Logger
from .routes import base, restricted

__all__: list[str] = ["Config", "create_app"]


def create_app() -> Flask:
    app: Flask = Flask(import_name=__name__)
    app.config.from_object(obj=Config)
    app.register_blueprint(blueprint=base)
    app.register_blueprint(blueprint=restricted)
    app.before_request(
        lambda: Logger.log_request(
            logger=Logger(
                log_directory=Config.LOG_DIRECTORY,
                log_file_name=Config.LOG_FILE_NAME,
            )
        )
    )
    return app
