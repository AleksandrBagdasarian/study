import time

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, nickname, password):
        self.data[nickname] = password
database = Database()
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age
        database.add_user(nickname, password)




class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = user

    def log_in(self, nickname, password ):
        pass


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        adult_mode = False

if __name__ == '__main__':
    u1 = User('Alex', 'Aleksandr', 29)
    u2 = User('Evi', '26.06.1997', 27)
    print(u1.nickname)
    print(database['Alex'])