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

if verify_database_connection():
    try:
        with app.app_context():
            db.create_all()
            print("Tablas creadas correctacmente")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")


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
