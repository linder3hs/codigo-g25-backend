from models.user import User, db
from models.role import Role

class UserController:

    @staticmethod
    def get_all_users():
        try:
            users = User.query.all()
            user_data = []

            for user in users:
                user_dict = user.to_dict()
                user_dict['roles'] = [role.to_dict() for role in user.roles]
                user_data.append(user_dict)

            return user_data, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.query.get(user_id)
            if user:
              user_dict = user.to_dict()
              user_dict['roles'] = [role.to_dict() for role in user.roles]
              return user_dict, None
            return None, "Usuario no encontrado"
        except Exception as e:
            return None, str(e)

    @staticmethod
    def create_user(data):
        try:
            exinting_user = User.query.filter_by(email=data.get("email")).first()

            if exinting_user:
                return None, "Hubo un error al crear el usuario"

            new_user = User(
                name=data.get('name'),
                lastname=data.get('lastname'),
                email=data.get('email'),
                password=data.get('password')
            )

            db.session.add(new_user)
            db.session.commit()

            return new_user.to_dict(), None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def update_user(user_id, data):
        try:
            user = User.query.get(user_id)

            if not user:
                return None, "Hubo un error al actualizar el usuario"

            if data.get("name"):
                user.name = data.get("name")
            if data.get("lastname"):
                user.lastname = data.get("lastname")
            if data.get("email"):
                user.email = data.get("email")
            if data.get("password"):
                user.password = data.get("password")

            db.session.commit()

            return user.to_dict(), None
        except Exception as e:
          return None, str(e)

    @staticmethod
    def delete_user(user_id):
        # Sof delete (Eliminado por cambio de status)
        try:
            user = User.query.get(user_id)

            if not user:
                return None, "Hubo un error al actualizar el usuario"

            user.is_active = False
            db.session.commit()

            return "Usuario desactivado correctamente", None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def asign_role(user_id, role_id):
        try:
            user = User.query.get(user_id)
            role = Role.query.get(role_id)

            if not user or not role:
                return None, "El usuario y el role son requeridos"

            if role not in user.roles:
                user.roles.append(role)
                db.session.commit()

                return "Role asignado correctamente", None
            else:
                return None, "El usuario ya tiene este role"
        except Exception as e:
            return None, str(e)
