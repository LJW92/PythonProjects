class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1





user_1 = User(1, 'jack')
print(user_1)
