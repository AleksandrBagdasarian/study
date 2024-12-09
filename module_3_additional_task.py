# Вариант 1 каждый тип данных в отдельном условии
def calculate_structure_sum(data):
    """
    Функция будет запускать проверку раз за разом пока по итогу не получит значение типа int или str
    """
    # Вводим переменную - счетчик, который будет в себе собирать сумму всего
    amount = 0
    # Условия начинаем с самого сложного и уникального (не итерируемый)
    if isinstance(data, dict):
        for key, value in data.items():
            amount += calculate_structure_sum(key)
            amount += calculate_structure_sum(value)
    # 3 одинаковых условия для списков, кортежей, и множеств
    elif isinstance(data, list):
        for i in data:
            amount += calculate_structure_sum(i)
    elif isinstance(data, set):
        for j in data:
            amount += calculate_structure_sum(j)
    elif isinstance(data, tuple):
        for k in data:
            amount += calculate_structure_sum(k)
    # 2 одинаковых условия для целых чисел и чисел с плавающей точкой
    elif isinstance(data, int):
        amount += data
    elif isinstance(data, float):
        amount += data
    # условие для строчки
    elif isinstance(data, str):
        amount += len(data)
    return amount

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)

# Вариант 2 объединение похожих процессов
def calculate_structure_sum_2(data_2):
    """
    Функция будет запускать проверку раз за разом пока по итогу не получит значение типа int или str
    """
    amount_2 = 0
    if isinstance(data_2, dict):
        for key_2, value_2 in data_2.items():
            amount_2 += calculate_structure_sum_2(key_2)
            amount_2 += calculate_structure_sum_2(value_2)
    elif isinstance(data_2, (list, set, tuple)):
        for i in data_2:
            amount_2 += calculate_structure_sum_2(i)
    elif isinstance(data_2, (int, float)):
        amount_2 += data_2
    elif isinstance(data_2, str):
        amount_2 += len(data_2)
    return amount_2

data_structure_2 = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result_2 = calculate_structure_sum_2(data_structure_2)
print(result_2)