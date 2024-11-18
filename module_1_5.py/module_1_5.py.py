immutable_var = (10 , 15 , '18.11.2024' , True , [99, 98] )
print(immutable_var)
# пробуем изменить значение кортежа
# immutable_var [2] = '19.11.2024'
# print(immutable_var)
# попытка изменить значение кортежа привела к ошибке, так как кортеж не поддерживает обращение по элементам
# при этом можно изменить значение списка, который является частью кортежа
immutable_var[4][1] = str('modify')
print(immutable_var)
mutable_list = [10 , 15 , '18.11.2024' , True , [99, 98]]
print(mutable_list)
# меняем значение 3 элемента списка
mutable_list [2] = '19.11.2024'
# добавляем в конец новый элемент с помощью команды Append
mutable_list.append ('Append')
print(mutable_list)
# добавляем в конец с помощью команды extend (чтобы добавилось значение, а не символы, добавляем как список)
mutable_list.extend(['Extend'])
print(mutable_list)
# удаляем значение из списка с помощью команды remove, используем индекс значения которое нужно удалить
mutable_list.remove(mutable_list[1])
print(mutable_list)
# проверяем наличие определенного значения в списке команда in
print('Append' in mutable_list)
# проверяем отсутствие определенного значения в списке команда not in
print('Extend' not in mutable_list)
# выводим часть списка с помощью индексов
print(mutable_list[2:5])
# выводим часть списка с помощью индексов с шагом 2
print(mutable_list[::2])