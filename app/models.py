from flask_login import UserMixin, LoginManager
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import login

@login.user_loader
def load_user(id):
    #return User.get(int(id))
    return User(1, 'Admin', 'passwd')


class User(UserMixin):
    id = 0
    username = 0
    usr_password = 0

    def __init__(self, id, uname, passw):
        self.id = id
        self.username = uname
        self.usr_password = passw

    def get(self,id):
        return self

    def set_password(self, password):
        self.usr_password = password

    def check_password(self, password):
        return self.usr_password == password

    def __repr__(self):
        return '<User {}>'.format(self.username)
