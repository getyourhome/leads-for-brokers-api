from flask import request
from flask_restful import Resource

from ..services.login import LoginService


class Login(Resource):
    def post(self):
        user_data = request.json

        service = LoginService()
        response = service.login(user_data["email"], user_data["password"])

        return response
