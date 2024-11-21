from flask import Blueprint, abort, request
from flask.wrappers import Response

from ..classes import Config, Token

restricted: Blueprint = Blueprint(name="restricted", import_name=__name__)


@restricted.before_request
def check_secret_key() -> None:
    secret_key: str = request.headers.get("X-Secret-Key", "")
    if secret_key != Config.SECRET_KEY:
        abort(403, "Access denied.")


@restricted.route("/flag", methods=["GET"])
def flag() -> Response:
    token: str = request.cookies.get("token", "")

    if Token.get_status(token) == Token.STATUS.INVALID:
        return Response("Invalid token.")
    elif Token.get_status(token) == Token.STATUS.PRIVILEGED:
        return Response(Config.FLAG)
    else:
        return Token.set_cookie("Token updated.", privileged=True)
