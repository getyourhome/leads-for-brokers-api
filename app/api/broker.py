from flask import jsonify, request
from flask_restful import Resource

from .auth import broker_auth
from ..services.broker_register import RegisterService


class Brokers(Resource):
    def post(self):
        broker_register = RegisterService()
        broker_response = broker_register.create(request.json)

        response = jsonify({"id": broker_response.id})
        response.status_code = 201
        return response


class Broker(Resource):
    @broker_auth.login_required
    def put(self, id):
        response = jsonify({"id": id})
        return response


class BrokerListings(Resource):
    @broker_auth.login_required
    def get(self):
        response = jsonify({"id": 1})
        return response
