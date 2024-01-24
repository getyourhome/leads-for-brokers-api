from flask import current_app
from flask_httpauth import HTTPTokenAuth
import jwt

token_auth = HTTPTokenAuth(scheme="Bearer")

# Temp - user registration todo
allowed_users = ["veloz@gmail.com"]


@token_auth.verify_token
def verify_token(token):
    secret_key = current_app.config["SECRET_KEY"]

    try:
        decoded_jwt = jwt.decode(token, secret_key, algorithms=["HS256"])
    except Exception as e:
        return None

    if decoded_jwt["email"] in allowed_users:
        return decoded_jwt
