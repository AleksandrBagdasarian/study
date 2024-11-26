# Вариант 1 цикл while
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
index = 0
new_list = []
while index < len(a):
    if a[index] < 50:
        new_list.append(a[index])
    index += 1
print(new_list)
# Вариант 2 цикл for
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for i in a:
    if i < 50:
        new_list.append(i)
print(new_list)
