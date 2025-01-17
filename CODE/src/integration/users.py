
class UserSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = password
        return "User registered"

    def authenticate_user(self, username, password):
        if self.users.get(username) == password:
            return "Authentication successful"
        return "Authentication failed"

# adicionar o erro se o usuario não existir