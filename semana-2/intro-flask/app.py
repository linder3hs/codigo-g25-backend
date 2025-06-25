from flask import Flask
from database import setup_database
from config import Config
from routes.user_routes import user_blueprint
from routes.post_routes import post_blueprint
from models.role import Role


app = Flask(__name__)

app.config.from_object(Config)

setup_database(app)

prefix = '/api/v1'

app.register_blueprint(user_blueprint, url_prefix=prefix)
app.register_blueprint(post_blueprint, url_prefix=prefix)

if __name__ == "__main__":
    app.run(debug=True)
