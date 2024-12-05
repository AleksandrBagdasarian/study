def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=[1, 2, 3], c=False)
print_params(b=25)
print_params(a=[0, 0, 0], b=[0, 0, 0], c=[0, 0, 0])

values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'string', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)