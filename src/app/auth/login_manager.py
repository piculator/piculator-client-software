from app.utils.singleton import singleton
from .user import User


@singleton
class LoginManager:
    def __init__(self):
        self.logged_in = False
        self.is_guest = True
        self.user = User('guest')
        self.last_login_status = None

    def auto_login(self):
        self.logged_in = True
        return True

    def login(self):
        return True


