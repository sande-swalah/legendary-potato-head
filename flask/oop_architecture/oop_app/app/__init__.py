from flask import Flask
from app.controllers.user_routes import user_blueprint

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(user_blueprint)

    return app
