# 1st program
from pprint import PrettyPrinter

print((9 ** 0.5)*5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))
print((2 * 2 + 2) == (2 * (2 + 2)))

# 4th program
x = float('123.456') # ввожу переменную равную 123,456
x1 = x * 10          # переношу запятую на 1 знак вправо
x = x1               # перезаписываю значение переменной x
x1 = x % 10          # находим остаток от деления на 10
print(int(x1))       # меняем тип переменной на int и выводим результат