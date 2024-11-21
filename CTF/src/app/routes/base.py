from flask import Blueprint, abort, request
from flask.wrappers import Response

from ..classes import Network, NetworkError, Token

base: Blueprint = Blueprint(name="base", import_name=__name__)


@base.route("/", methods=["GET"])
def index() -> Response:
    return Token.set_cookie("New token granted.", privileged=False)


@base.route("/fetch", methods=["POST"])
def fetch() -> Response:
    token: str = request.cookies.get("token", "")
    url: str = request.get_data().decode("utf-7")

    if Token.get_status(token) == Token.STATUS.INVALID:
        abort(403, "Token is either invalid or expired.")
    elif error_message := Network.is_invalid_url(url, token):
        abort(400, error_message)

    try:
        return Network.fetch(url, token)
    except NetworkError as error:
        abort(500, str(error))
    except Exception:
        abort(500, "An unexpected error occurred while fetching the resource.")
