from datetime import datetime, UTC
from database import db
from user_role import user_roles
import re

class User(db.Model):
    # indicar el nombre de la tabla
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=True)
    lastname = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # nuevos campos
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    email_verified = db.Column(db.Boolean, default=False, nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    failed_login_attempts = db.Column(db.Integer, default=0, nullable=False)
    # se coloca los campos fecha_creacion fecha_actualizacion
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    updated_at = db.Column(db.DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))

    posts = db.relationship('Post', backref='author', lazy=True, cascade='all, delete-orphan')
    roles = db.relationship('Role', secondary=user_roles, back_populates='users')

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email.lower().strip()
        self.password = password

    def to_dict(self, show_password=False):
        user_dict = {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_active": self.is_active,
            "email_verified": self.email_verified,
            "last_login": self.last_login,
            "failed_login_attempts": self.failed_login_attempts
        }

        if show_password:
            user_dict['password'] = self.password

        return user_dict

    def parse_fullname(self):
        return f"{self.name} {self.lastname}"

    @staticmethod
    def validate_emal(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None

    @staticmethod
    def validate_password(password):
        # validamos cantidad de caracteres
        if len(password) < 8:
            return False, 'La contraseña debe tener al menos 8 caracteres.'

        if not re.search(r'[A-Z]', password):
            return False, 'La contraseña debe contener al menos una letra mayúscula.'

        if not re.search(r'[a-z]', password):
            return False, 'La contraseña debe contener al menos una letra minúscula.'

        if not re.search(r'\d', password):
            return False, 'La contraseñ debe contener al menu un número.'

        return True, 'Contraseñ válida'
