

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def print(self):
        print(f"User {self.username} has {self.followers} followers and follow {self.following} peoples" )


def main():
    user1 = User("001", "TeaYang")
    user2 = User("002", "GD")
    user2.follow(user1)
    user1.print()
    user2.print()


if __name__ == '__main__':
    main()

