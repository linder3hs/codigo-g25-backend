from flask import Blueprint, jsonify, request
from controllers.auth_controller import AuthController

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
  try:
      data = request.get_json()

      if not data:
         return jsonify({"error": "Los datos de registro son requeridos"}), 400

      result, error = AuthController.register_user(data)

      if error:
         return jsonify({"error": error}), 403

      return jsonify({
         "message": "Usuario registrado correctamente",
         "user": result
      })
  except Exception as e:
      return jsonify({
        "error": f"Error: {e}"
      }), 500

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Los datos de registro son requeridos"}), 400

        email = data.get('email')
        password = data.get('password')

        result, error = AuthController.authenticate_user(email, password)

        if error:
            return jsonify({"error": error}), 403

        return jsonify({
           "message": "Usuario autenticado correctamente",
         "user": result
        })

    except Exception as e:
      return jsonify({
        "error": f"Error: {e}"
      }), 500
