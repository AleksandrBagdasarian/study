my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
my_new_list = []
while index < len(my_list):
    if my_list[index] < 0:
        break
    if my_list[index] > 0:
        my_new_list.append(my_list[index])
    index += 1
print(my_new_list)