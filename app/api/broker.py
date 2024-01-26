from flask import Blueprint, jsonify, request

from .auth import token_auth
from ..services.broker_register import RegisterService


broker_bp = Blueprint("broker", __name__, url_prefix="/broker")


@broker_bp.route("/", methods=["POST"])
def create_broker():
    broker_register = RegisterService()
    broker_response = broker_register.create(request.json)

    response = jsonify({"id": broker_response.id})
    response.status_code = 201
    return response


@broker_bp.route("/<id>", methods=["PUT"])
@token_auth.login_required
def update_broker(id):
    response = jsonify({"id": id})
    response.status_code = 201
    return response


@broker_bp.route("/listings", methods=["GET"])
@token_auth.login_required
def listings():
    response = jsonify({"id": 1})
    return response
