# Вариант 1 цикл while
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
index = 0
new_list = []
while index < len(a):
    if a[index] < 100:
        new_list.append(a[index])
    index += 1
print(new_list)
# Вариант 2 цикл for
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for i in range(len(a)):
    if a[i] < 50:
        new_list.append(a[i])
print(new_list)
# Последовательность Фибаначи
my_fib_list = []
n = int(input('Введите количество чисел в последовательности Фибаначи '))
for i in range(n):
    if i == 0 or i == 1:
        my_fib_list.append(1)
        continue
    value = my_fib_list[i - 1] + my_fib_list[i - 2]
    my_fib_list.append(value)
print(my_fib_list)
# Последовательность Фибаначи программа
def my_fib(n):
    new_list = []
    for i in range(n):
        if i == 0 or i == 1:
            new_list.append(1)
        else:
            new_list.append(new_list[i-1] + new_list[i - 2])
    return new_list
n = int(input('Введите количество числе в последовательности Фибаначи: '))
list_of_fib = my_fib(n)
print(list_of_fib)