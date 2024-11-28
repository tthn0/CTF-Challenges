from os import getenv
from pathlib import Path

from dotenv import find_dotenv, load_dotenv


class Config:
    # Load default environment variables if FLASK_ENV is missing
    FLASK_ENV: str = getenv("FLASK_ENV", "")
    if not FLASK_ENV:
        load_dotenv(find_dotenv(".env.development"))

    # Flask config values
    SECRET_KEY: str = getenv("SECRET_KEY", "")
    DEBUG: bool = FLASK_ENV != "production"

    # Custom config values
    DOMAIN_REGEX: str = getenv("DOMAIN_REGEX", "")
    FLAG: str = getenv("FLAG", "")
    PORT: int = int(getenv("PORT", ""))
    LOG_FILE_NAME: str = getenv("LOG_FILE_NAME", "")
    LOG_DIRECTORY_NAME: str = getenv("LOG_DIRECTORY_NAME", "")
    LOG_DIRECTORY: Path = (
        Path(__file__).parent.parent.parent.parent / LOG_DIRECTORY_NAME
    )

    if not all(
        (
            SECRET_KEY,
            DOMAIN_REGEX,
            FLAG,
            PORT,
            LOG_FILE_NAME,
            LOG_DIRECTORY_NAME,
        )
    ):
        raise ValueError("Some environment variables are missing.")
