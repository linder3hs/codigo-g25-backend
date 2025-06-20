import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from user import User, db
from sqlalchemy import text

# Cargar credenciales secretas
load_dotenv()

# instanciar Flask
app = Flask(__name__)

# Vamos a crear la URL de conection a la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)

def verify_database_connection():
    try:
        with app.app_context():
            result = db.session.execute(text('SELECT 1'))
            result.fetchone()
            print("Connection Success")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

verify_database_connection()
users = []

# por defecto todas las rutas son GET
@app.route("/")
def home():
    return jsonify({
        "message": "Home de mi app",
        "status": 200
    })

@app.route("/api/v1/users")
def get_user():
    try:
        # crear una lista para poder convertir mi
        # arreglo de instancias a un arreglo de dicts
        user_list = []

        for user in users:
            user_list.append(user.to_dict())

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
        for user in users:
            if user.id == user_id:
                return jsonify({
                    "message": "Busqueda por usuario",
                    "user": user.to_dict()
                })

        return jsonify({
            "message": "Usuario no encontrado"
        })
    except Exception as e:
        return jsonify({
          "error": str(e)
        }),

@app.route("/api/v1/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        # creamos la instancia con la clase user
        id = len(users) + 1
        new_user = User(
            id,
            data.get("name"),
            data.get("lastname"),
            data.get("email"),
            data.get("password")
        )

        users.append(new_user)
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

        # Buscar el usuario por ID
        for user in users:
            if user.id == user_id:
                # Actualizar solo los campos que se envían en el request
                if data.get("name"):
                    user.name = data.get("name")
                if data.get("lastname"):
                    user.lastname = data.get("lastname")
                if data.get("email"):
                    user.email = data.get("email")
                if data.get("password"):
                    user.password = data.get("password")

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
        for index, user in enumerate(users):
            if user.id == user_id:
                users.pop(index)
                return jsonify({
                    "message": "Usuario eliminado"
                })

        return jsonify({
            "message": "Usuario no encontrado"
        })
    except Exception as e:
        return jsonify({
          "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
