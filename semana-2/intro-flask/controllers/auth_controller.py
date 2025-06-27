from models.user import User, db
from models.role import Role
from datetime import datetime, UTC
from utils.password_manager import PasswordManager
from utils.token_manager import TokenManager

class AuthController:

    @staticmethod
    def register_user(data):
        try:
            validation_error = AuthController._validate_registration_data(data)
            if validation_error:
                return None, validation_error

            existing_user = User.query.filter_by(email=data.get('email').lower().strip()).first()

            if existing_user:
                return None, 'El email ya esta registrados'

            password_valid, password_message = PasswordManager.validate_password(data.get('password'))
            if not password_valid:
                return None, password_message

            new_user = User(
                name=data.get('name').strip(),
                lastname=data.get('lastname').strip(),
                email=data.get('email').lower().strip(),
                password=data.get('password')
            )
            default_role = Role.query.filter_by(name='USER').first()

            if default_role:
                new_user.roles.append(default_role)

            db.session.add(new_user)
            db.session.commit()

            access_token = TokenManager.generate_token(new_user.id)

            response = {
                "user": new_user.to_dict(),
                "access_token": access_token,
                "token_type": "Bearer"
            }

            return response, None
        except Exception as e:
            db.session.rollback()
            return None, f"Error: {e}"

    @staticmethod
    def authenticate_user(email, password):
        try:
            if not email or not password:
                return None, "Email y Password son requeridos"

            user = User.query.filter_by(email=email.lower().strip()).first()

            if not user:
                return None, 'Usuario no encontrado'

            if not user.check_password(password):
                user.failed_login_attempts += 1
                db.session.commit()
                return None, 'El password no coincide'

            user.failed_login_attempts = 0
            user.last_login = datetime.now(UTC)
            db.session.commit()

            access_token = TokenManager.generate_token(user.id)

            response = {
                "user": user.to_dict(),
                "access_token": access_token,
                "token_type": "Bearer",
                "message": "Autenticación correcta"
            }

            return response, None
        except Exception as e:
            return None, f"Error: {e}"

    @staticmethod
    def _validate_registration_data(data):
        required_fields = ['name', 'lastname', 'email', 'password']

        for field in required_fields:
            if not data.get(field) or not data.get(field).strip():
                return f"El campo {field} es requerido."

        if not User.validate_email(data.get('email')):
            return "Formato de correo invalido"

        return None
