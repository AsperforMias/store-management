
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, password):
        return self.password == password

    def __repr__(self):
        return self.username