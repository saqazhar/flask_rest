from werkzeug.security import safe_str_cmp
from models.myuser import User


def authenticate(username, password):
    new_user = User.find_by_username(username)
    if new_user and safe_str_cmp(new_user.password, password):
        return new_user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
 