import random

# Задаем случайное присвоение первого числа из диапазона с 3 до 20
first_digit = random.randint(3, 20)
# Выводим значение первого числа
print('Первое число: ', first_digit)
# Создаем список для подбора пароля длиной как переменная first_digit, больше нет смысла пары повторяются.
selection_list = list(range(1, first_digit))
# Создаем пустой список в который программа будет собирать пароль
second_digits = []


# Создаем функцию, которая будет подбирать пароль
def сhristopher_jr():
    #Первый цикл для первого значения в списке подбора пароля
    for i in range(first_digit):
        # Второй цикл для перебора значений того же списка начиная по следующего исключая само число
        for j in range(i + 1, first_digit - 1):
            # Проверка кратности - деление без остатка суммы 2-х последовательных элементов списка
            if first_digit % (selection_list[i] + selection_list[j]) != 0:
                # Возвращаем цикл в начало, если условие не соблюдено
                continue
            # Если условие соблюдено, добавляем соответствующие значения в конечный список
            else:
                second_digits.append(selection_list[i])
                second_digits.append(selection_list[j])
    # Возвращаем готовый список
    return second_digits

# Вызываем функцию
result = сhristopher_jr()
# Выводим результат без скобок и пробелов
print('Пароль: ', *result, sep='')