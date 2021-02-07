class User:
    def __init__(self, username):
        self.username = username

    @property
    def is_guest(self):
        return self.username == 'guest'
