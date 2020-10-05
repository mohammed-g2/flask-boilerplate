from flask_login import UserMixin, AnonymousUserMixin
from app import db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)


class AnonymousUser(AnonymousUserMixin):
    pass


login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
