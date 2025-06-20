from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    # indicar el nombre de la tabla
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=True)
    lastname = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    # se coloca los campos fecha_creacion fecha_actualizacion
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def parse_fullname(self):
        return f"{self.name} {self.lastname}"
