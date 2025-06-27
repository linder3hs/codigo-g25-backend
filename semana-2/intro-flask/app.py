from flask import Flask
from database import setup_database
from config import Config
from flask_jwt_extended import JWTManager
from routes.user_routes import user_blueprint
from routes.post_routes import post_blueprint
from routes.auth_routes import auth_blueprint
from models.role import Role


app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)

setup_database(app)

prefix = '/api/v1'

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    print({"jwt_header":jwt_header, "jwt_payload": jwt_payload})
    return {
        "error": "Token expirado",
        "message": "Iniciar session nuevamente para generar uno nuevo"
    }, 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    print(f"invalid_token_callback Error: {error}")
    return {
        "error": error
    }, 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    print(f"missing_token_callback Error: {error}")
    return {
        "error": error
    }, 401

app.register_blueprint(user_blueprint, url_prefix=prefix)
app.register_blueprint(post_blueprint, url_prefix=prefix)
app.register_blueprint(auth_blueprint, url_prefix=prefix)

if __name__ == "__main__":
    app.run(debug=True)
