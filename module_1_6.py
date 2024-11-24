my_dict = {'Alex': 1995, 'Evi': 1997, 'Lana': 2024}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Ivan', 'Такого человека нет в справочнике'))
my_dict.update({'Ani': 1988,
                'Nelly': 1986})
del my_dict['Alex']
print(my_dict)

my_set = {5, 5, 5, 4, 4, 3, 2, 2, 3, 5}
print(my_set)
# Чтобы добавить сразу несколько значений в множество через update(обязательно список в [] скобках)
my_set.update(['A', 7, True])
my_set.discard(5)
print(my_set)