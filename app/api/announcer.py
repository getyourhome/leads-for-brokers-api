from flask import Blueprint, jsonify, request

from ..services.announcer_register import RegisterService
from .auth import token_auth


announcer_bp = Blueprint("announcer", __name__, url_prefix="/announcer")


@announcer_bp.route("/register", methods=["POST"])
def register():
    ad_register = RegisterService()
    ad_response = ad_register.create(request.json)

    response = jsonify({"id": ad_response.id})
    response.status_code = 201
    return response


@announcer_bp.route("/ad/<id>", methods=["PUT"])
@token_auth.login_required
def update_ad(id):
    response = jsonify({"id": id})
    return response


@announcer_bp.route("/ad/<id>", methods=["GET"])
@token_auth.login_required
def get_ad(id):
    response = jsonify({"id": id})
    return response
