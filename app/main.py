from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_app(testing: bool = False):
    app = Flask(__name__)

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
