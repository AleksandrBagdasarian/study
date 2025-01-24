import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode = False):
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

    def add(self, *videos):
        for vid in videos:
            if not any(i.title == vid.title for i in self.videos):
                self.videos.append(vid)

    def get_videos(self, word):
        word_low = word.lower()
        search_list = []
        for i in self.videos:
            if word_low in i.title.lower():
                search_list.append(i.title)
        return search_list

    # def watch_video(self, name):
    #     for i in self.videos:
    #         if name == i.title:
    #             print






if __name__ == '__main__':
    ur = UrTube()
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.log_out()
    print(ur.current_user)
    ur.log_in('vasya_pupkin','lolkekcheburek')
    print(ur.current_user)
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
    print(v1.title)
    ur.add(v1, v2)
    print(ur.videos)
