from .announcer import announcer_bp
from .access import access_bp
from .broker import broker_bp


def init_app(app):
    app.register_blueprint(announcer_bp)
    app.register_blueprint(broker_bp)
    app.register_blueprint(access_bp)
