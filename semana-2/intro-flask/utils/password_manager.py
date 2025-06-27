import bcrypt
import re

class PasswordManager:

    @staticmethod
    def hash_password(password):
        """
        Genera un passwod hasheado
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(password, hashed_password):
        """
        Verificar si el password que envia el cliente hacer match con el password de la base de datos
        """
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception:
            return False

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False, 'La contraseña debe tener al menos 8 caracteres.'

        if not re.search(r'[A-Z]', password):
            return False, 'La contraseña debe contener al menos una letra mayúscula.'

        if not re.search(r'[a-z]', password):
            return False, 'La contraseña debe contener al menos una letra minúscula.'

        if not re.search(r'\d', password):
            return False, 'La contraseñ debe contener al menu un número.'

        return True, 'Contraseñ válida'
