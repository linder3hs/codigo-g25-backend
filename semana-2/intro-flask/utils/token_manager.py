from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import datetime, UTC

class TokenManager:

    @staticmethod
    def generate_token(user_id):
        new_token = create_access_token(identity=str(user_id), additional_claims={
            'created_at': datetime.now(UTC).isoformat()
        })
        return new_token

    @staticmethod
    def get_current_user_id():
        return get_jwt_identity()
