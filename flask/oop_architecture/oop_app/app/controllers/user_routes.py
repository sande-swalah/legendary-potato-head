from flask import Blueprint, jsonify
from app.services.user_service import UserService

user_blueprint = Blueprint("users", __name__)

service = UserService()

@user_blueprint.route("/")
def home():
    return jsonify({"message": "Flask OOP API"})

@user_blueprint.route("/users")
def users():
    return jsonify(service.get_all_users())

@user_blueprint.route("/users/<int:user_id>")
def get_user(user_id):
    user = service.get_user(user_id)

    if user:
        return jsonify(user)

    return jsonify({"error": "User not found"}), 404
