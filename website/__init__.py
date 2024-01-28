from flask import Flask
from os import path


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dinner"

    from .dinner import dinner

    app.register_blueprint(dinner, url_prefix="/")

    return app
