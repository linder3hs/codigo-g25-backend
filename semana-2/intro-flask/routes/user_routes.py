from flask import Blueprint, jsonify, request
from controllers.user_controller import UserController

# crear el Blueprint
user_blueprint = Blueprint('users', __name__)

# data(users), error
@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users, error = UserController.get_all_users()

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Lista de usuarios",
        "users": users
    })

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user, error = UserController.get_user_by_id(user_id)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Usuario encontrado",
        "user": user
    })

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    user, error = UserController.create_user(data)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Usuario creado",
        "user": user
    })

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    user, error = UserController.update_user(user_id, data)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Usuario actualizado",
        "user": user
    })

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success, error = UserController.delete_user(user_id)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": success,
    })
