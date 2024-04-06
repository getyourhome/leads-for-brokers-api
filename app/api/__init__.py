from flask_restful import Api
from flask import Blueprint

from .access import Login
from .announcer import Announcers, Announcer
from .broker import Broker, Brokers, BrokerListings


bp = Blueprint("restapi", __name__, url_prefix="/api")
api = Api(bp)

api.add_resource(Announcers, "/announcer")
api.add_resource(Announcer, "/announcer/<string:id>")

api.add_resource(Brokers, "/broker")
api.add_resource(Broker, "/broker/<string:id>")
api.add_resource(BrokerListings, "/broker/listings")

api.add_resource(Login, "/login")


def init_app(app):
    app.register_blueprint(bp)
