from app.models.user_model import User

class UserService:

    def __init__(self):
        self.users = [
            User(1, "Alice"),
            User(2, "Bob"),
            User(3, "Charlie")
        ]

    def get_all_users(self):
        return [user.to_dict() for user in self.users]

    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user.to_dict()
        return None
