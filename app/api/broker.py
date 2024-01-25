from flask import Blueprint, jsonify, request

from .auth import token_auth


broker_bp = Blueprint("broker", __name__, url_prefix="/broker")


@broker_bp.route("/", methods=["POST"])
def create_broker():
    response = jsonify({"id": 1})
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
