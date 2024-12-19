# class User:
#     pass

# user_1 = User()
# user_1.id = "001"
# user_1.username = "ps"

# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.name = "jack"

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "ps")

print(user_1.followers)

