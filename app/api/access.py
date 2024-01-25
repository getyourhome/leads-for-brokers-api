from flask import Blueprint, current_app, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt


access_bp = Blueprint("access", __name__)


@access_bp.route("/login", methods=["POST"])
def login():
    user_data = request.json
    secret_key = current_app.config["SECRET_KEY"]

    if "email" not in user_data or "password" not in user_data:
        raise Exception("Unable to authenticate")

    temp_password = generate_password_hash("todo")

    if not check_password_hash(temp_password, user_data["password"]):
        raise Exception("Invalid password")

    encoded_jwt = jwt.encode(
        {"user_id": 1, "email": user_data["email"]},
        secret_key,
        algorithm="HS256",
    )

    return jsonify({"token": encoded_jwt})
