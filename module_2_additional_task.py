import random

first_digit = random.randint(3, 20)
print('Первое число: ', first_digit)
selection_list = list(range(1, first_digit))
second_digits = []


# Создаем функцию, которая будет подбирать пароль
def сhristopher_jr():
    for i in range(first_digit):
        for j in range(i + 1, first_digit - 1):
            if first_digit % (selection_list[i] + selection_list[j]) != 0:
                continue
            else:
                second_digits.append(selection_list[i])
                second_digits.append(selection_list[j])
    return second_digits


result = сhristopher_jr()
print('Пароль: ', *result, sep='')
