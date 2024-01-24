from flask import jsonify, request
from flask_restful import Resource

from ..services.property import PropertyService


class PropertyResource(Resource):
    def post(self):
        property = PropertyService()
        property_response = property.create(request.json)

        response = jsonify({"id": property_response.id})
        response.status_code = 201
        return response
