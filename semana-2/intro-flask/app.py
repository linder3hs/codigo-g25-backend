from flask import Flask
from models.post import Post
from database import setup_database
from config import Config
from routes.user_routes import user_blueprint

app = Flask(__name__)

app.config.from_object(Config)

setup_database(app)

app.register_blueprint(user_blueprint, url_prefix='/api/v1')

if __name__ == "__main__":
    app.run(debug=True)
