from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
            return f"{self.nickname}"

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"{self.title}, duration - {self.duration}, adult_mode - {self.adult_mode})"


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

    def watch_video(self, name):
        video = None
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for i in self.videos:
            if name == i.title:
                video = i
        if not video:
            return
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for second in range(video.time_now, video.duration):
            print(f"Секунда: {second + 1}")
            sleep(1)
        video.time_now = 0
        print("Конец видео")


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
