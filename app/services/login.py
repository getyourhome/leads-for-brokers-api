from flask import jsonify, current_app
from sqlalchemy import select
from werkzeug.security import check_password_hash
import jwt

from ..data.models import db, User


class LoginService:
    def login(self, email, password):
        if email == "" or password == "":
            raise Exception("Please fill email and password")

        user = db.session.scalars(select(User).where(User.email == email)).one_or_none()

        if not user:
            raise Exception("Invalid email or password")
            # Possible approach for building validation
            # return jsonify({"error": "no user found in database"}), 404

        if not check_password_hash(user.password, password):
            raise Exception("Invalid  email or password")

        secret_key = current_app.config["SECRET_KEY"]

        encoded_jwt = jwt.encode(
            {"user_id": user.id, "email": user.email, "role": user.type.name},
            secret_key,
            algorithm="HS256",
        )

        return jsonify({"token": encoded_jwt})
