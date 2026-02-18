from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class user(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.string(120), unique=True, nullable=False)
    password_hash = db.Column(db.string(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
        return user.query.get(int(user_id))