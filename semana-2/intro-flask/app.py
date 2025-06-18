# importamos Flask
from flask import Flask, jsonify, request
from user import User

# instanciar Flask
app = Flask(__name__)

print(__name__) # __main__

# lista de usuarios
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


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        # creamos la instancia con la clase user
        new_user = User(
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



if __name__ == "__main__":
    app.run(debug=True)
