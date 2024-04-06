from flask import jsonify, request
from flask_restful import Resource

from ..services.announcer_register import RegisterService
from .auth import announcer_auth


class Announcers(Resource):
    def post(self):
        ad_register = RegisterService()
        ad_response = ad_register.create(request.json)

        response = jsonify({"id": ad_response.id})
        response.status_code = 201
        return response

    @announcer_auth.login_required
    def get(self):
        user_data = announcer_auth.current_user()

        response = jsonify({"id": user_data["user_id"]})
        return response


class Announcer(Resource):
    def get(self, id):
        response = jsonify({"id": id})
        return response
