# Создаем программу рассылки (вариант 1 endswith чувствительно к регистру окончания)
def send_email_1(message, recipient, sender = 'university.help@gmail.com'):
    # создаем 2 переменные для проверок: знак "@" и корректные окончания почты.
    # сразу регистр меняем на нижний
    sender = sender.lower()
    dog = '@'
    correct_ending = ('.com', '.ru', '.net')
    # Проверка окончания почты, endswith
    end_check = all([sender.endswith(correct_ending, -4), recipient.endswith(correct_ending, -4)])
    if end_check is False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # Проверка наличия собаки в почте (если будет собака в тексте, а не в конце программа пропустит)
    elif any([recipient.find(dog) == -1,  sender.find(dog) == -1]):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # Проверка отправки самому себе (приводим к одному регистру, иначе можно будет отправить если поменять одну букву
    elif recipient.lower() == sender.lower():
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    return message, recipient, sender
send_email_1('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email_1('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email_1('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email_1('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


# Создаем программу рассылки (вариант 2 без endswith так как чувствительно к регистру)
def send_email_2(message, recipient, sender = 'university.help@gmail.com'):
    # создаем 4 переменные для проверок: знак "@", корректные окончания почты, а также концы почт.
    # сразу регистр меняем на нижний
    sender = sender.lower()
    dog = '@'
    recipient_end = recipient[recipient.rfind('.'):]
    sender_end = sender[sender.rfind('.'):]
    correct_ending = ('.com', '.ru', '.net')
    # Проверка окончания почты, не чувствительно к регистру
    end_check = all([sender_end.lower() in correct_ending, recipient_end.lower() in correct_ending])
    if end_check is False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # Проверка наличия собаки в окончании почты
    elif any([recipient.find(dog) == -1,  sender.find(dog) == -1]):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient.lower() == sender.lower():
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    return message, recipient, sender
send_email_2('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email_2('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email_2('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email_2('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')