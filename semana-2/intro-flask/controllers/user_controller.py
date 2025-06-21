from models.user import User, db

class UserController:

    @staticmethod
    def get_all_users():
        try:
            users = User.query.all()
            return [user.to_dict() for user in users], None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.query.get(user_id)
            if user:
              return user.to_dict(), None
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
