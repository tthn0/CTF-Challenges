from datetime import datetime, timedelta, timezone
from enum import Enum, auto
from typing import Any

import jwt
from flask import Response, make_response

from .config import Config


class Token:
    KEY: str = Config.SECRET_KEY
    ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 60 * 60

    class STATUS(Enum):
        PRIVILEGED = auto()
        UNPRIVILEGED = auto()
        INVALID = auto()

    @staticmethod
    def _create(privileged: bool) -> str:
        return jwt.encode(
            payload={
                "privileged": privileged,
                "iat": datetime.now(timezone.utc),
                "exp": datetime.now(timezone.utc)
                + timedelta(seconds=Token.JWT_EXPIRATION_SECONDS),
            },
            key=Token.KEY,
            algorithm=Token.ALGORITHM,
        )

    @staticmethod
    def set_cookie(message: str, privileged: bool = False) -> Response:
        res: Response = make_response(message)
        res.set_cookie(
            key="token",
            value=Token._create(privileged),
            max_age=Token.JWT_EXPIRATION_SECONDS,
            httponly=True,
            samesite="Strict",
        )
        return res

    @staticmethod
    def get_status(token: str) -> STATUS:
        try:
            payload: dict[str, Any] = jwt.decode(
                jwt=token,
                key=Token.KEY,
                algorithms=[Token.ALGORITHM],
            )
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return Token.STATUS.INVALID

        if payload["privileged"]:
            return Token.STATUS.PRIVILEGED
        else:
            return Token.STATUS.UNPRIVILEGED
