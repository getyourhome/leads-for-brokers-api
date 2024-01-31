from flask import current_app
from flask_httpauth import HTTPTokenAuth
import jwt

from ..data.enums import UserRole


def create_auth(allowed_role):
    auth = HTTPTokenAuth(scheme="Bearer")

    @auth.verify_token
    def verify_token(token):
        secret_key = current_app.config["SECRET_KEY"]

        try:
            decoded_jwt = jwt.decode(token, secret_key, algorithms=["HS256"])
        except Exception as e:
            return None

        if decoded_jwt["role"] != allowed_role.name:
            return None

        return decoded_jwt

    return auth


broker_auth = create_auth(UserRole.broker)
announcer_auth = create_auth(UserRole.announcer)
