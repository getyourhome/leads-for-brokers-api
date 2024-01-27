from flask import Blueprint, current_app, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from ..services.login import LoginService


access_bp = Blueprint("access", __name__)


@access_bp.route("/login", methods=["POST"])
def login():
    user_data = request.json

    service = LoginService()
    response = service.login(user_data["email"], user_data["password"])

    return response
