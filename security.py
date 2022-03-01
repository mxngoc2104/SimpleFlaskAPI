from models.user import UserModel


def authenticate1(username, password):
    user = UserModel.find_by_user_name(username)
    if user and user.password == password:
        return user


def identity1(payload):
    user_id = payload['identity']
    return UserModel.find_by_user_id(user_id)
