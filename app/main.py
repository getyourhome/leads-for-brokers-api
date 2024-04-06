from flask import Flask
import os
from dotenv import load_dotenv
from flask_cors import CORS

import app.data as data
import app.api as api

# Load environment variables from .env file
load_dotenv()


def create_app(testing: bool = False):
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=os.environ["API_URL"])

    env_config = os.getenv("APP_SETTINGS")
    app.config.from_object(env_config)

    data.init_app(app)
    api.init_app(app)

    @app.route("/")
    def health_check():
        return "Server is ready"

    @app.route("/version")
    def api_version():
        version = os.environ["VERSION"]
        return f"API VERSION: {version}"

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
