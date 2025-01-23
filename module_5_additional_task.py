import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_out(self):
        self.current_user = None
        return

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                return
        print("Неверный логин или пароль")

    def register(self,nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname,password, age)
        self.users.append(new_user)
        self.current_user = new_user







if __name__ == '__main__':
    ur = UrTube()
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.log_out()
    print(ur.current_user)
    ur.log_in('vasya_pupkin','lolkekcheburek')
    print(ur.current_user)