from os import getenv

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

    if not all((SECRET_KEY, DOMAIN_REGEX, FLAG, PORT)):
        raise ValueError("Some environment variables are missing.")
