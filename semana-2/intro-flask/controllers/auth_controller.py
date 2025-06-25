from models.user import User, db
from models.role import Role

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

            password_valid, password_message = User.validate_password(data.get('password'))
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

        except Exception as e:
            db.session.rollback()
            return None, f"Error: {e}"

    @staticmethod
    def _validate_registration_data(data):
        required_fields = ['name', 'lastname', 'email', 'password']

        for field in required_fields:
            if not data.get(field) or not data.get(field).strip():
                return f"El campo {field} es requerido."

        if not User.validate_emal(data.get('email')):
            return "Formato de correo invalido"

        return None
