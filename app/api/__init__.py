from flask import Blueprint
from flask_restful import Api

from .property import PropertyResource


# Api routes registration
bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(PropertyResource, "/property")


def init_app(app):
    app.register_blueprint(bp)
