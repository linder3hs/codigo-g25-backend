from database import db
from datetime import datetime, UTC

user_roles = db.Table('user_roles',
                      db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                      db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
                      db.Column('assignet_at', db.DateTim, default=datetime.now(UTC), nullable=False),
                      )
