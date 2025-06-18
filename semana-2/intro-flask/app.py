# importamos Flask
from flask import Flask, jsonify

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
    return "Lista de usuarios"


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)
