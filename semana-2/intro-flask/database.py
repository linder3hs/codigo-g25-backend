from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def init_database(app):
    db.init_app(app)

def verify_database_connection(app):
    try:
        with app.app_context():
            result = db.session.execute(text('SELECT 1'))
            result.fetchone()
            print("Connection Success")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_tables(app):
    try:
        with app.app_context():
            db.create_all()
            print("Se crearon las tablas")
    except Exception as e:
        print(f"Errora al crear tablas: {e}")
        return False

def setup_database(app):
    init_database(app)

    if verify_database_connection(app):
        create_tables(app)
        return True
    else:
        print("Hubo un error al conectarnos a la base de datos")
        return False
