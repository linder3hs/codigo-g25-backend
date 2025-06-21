import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from models.user import User
from models.post import Post
from database import setup_database, db
from config import Config

# Cargar credenciales secretas
load_dotenv()

# instanciar Flask
app = Flask(__name__)

app.config.from_object(Config)

setup_database(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Home de mi app",
        "status": 200
    })

@app.route("/api/v1/users")
def get_user():
    try:
        # SELECT * FROM users
        users = User.query.all()
        user_list = [user.to_dict() for user in users]

        return jsonify({
              "message:": "Lista de usuarios",
              "users": user_list
            })
    except Exception as e:
      return jsonify({
          "error": str(e)
        }), 500


@app.route("/api/v1/users/<int:user_id>", methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            return jsonify({
                "message": "Usuario encontrado",
                "user": user.to_dict()
            })
        else:
            return jsonify({
                "message": "Usuario no encontrado"
            }), 404
    except Exception as e:
        return jsonify({
          "error": str(e)
        }),

@app.route("/api/v1/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        # validar que el correo no exista
        existing_user = User.query.filter_by(email=data.get("email")).first()

        if existing_user:
            return jsonify({
                "error": "Hubo un error al crear el usuario"
            })

        new_user = User(
            name=data.get("name"),
            lastname=data.get("lastname"),
            email=data.get("email"),
            password=data.get("password")
        )

        # Guarde la informacion en la DB
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "Usuario creado",
            "user": new_user.to_dict()
        }), 201
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        user = User.query.get(user_id)

        if not user:
            return jsonify({
                "message": "Hubo un error"
            }), 404

        if data.get("name"):
            user.name = data.get("name")
        if data.get("lastname"):
            user.lastname = data.get("lastname")
        if data.get("email"):
            user.email = data.get("email")
        if data.get("password"):
            user.password = data.get("password")

        db.session.commit()

        return jsonify({
            "message": "Usuario actualizado",
            "user": user.to_dict()
        }), 200

        # Si no se encuentra el usuario
        return jsonify({
            "message": "Usuario no encontrado"
        }), 404

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user:
            return jsonify({
                "message": "Usuario no encontrado"
            }), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({
            "message": "Usuario eliminado correctamente"
        })
    except Exception as e:
        return jsonify({
          "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
