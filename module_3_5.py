# Нули превращаем в 1 произведение не меняется
def get_multiplied_digits(number):
    str_number = str(number)
    first = str_number[0]
    if len(str_number) > 1:
        return int(first) * get_multiplied_digits(int(str_number[1:]))
    # Условие которое в случае если число = 0 меняет его на 1
    elif int(first) == 0:
        return 1
    return int(first)

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)

# Изначально убираем все нули из заданного числа
def get_multiplied_digits_2(number_2):
    str_number_2 = str(number_2)
    # "Очищаем" строку от нулей
    clear_str = str_number_2.replace('0','')
    first_2 = clear_str[0]
    if len(clear_str) > 1:
        return int(first_2) * get_multiplied_digits_2(int(clear_str[1:]))
    return int(first_2)
result = get_multiplied_digits_2(40203)
print(result)
result2 = get_multiplied_digits_2(402030)
print(result2)