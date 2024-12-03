# Переменная которая будет считать количество вызовов
calls = 0
# Программа для подсчета, ссылаемся на переменную из глобального пространства имен
def count_calls ():
      global calls
      calls += 1
# Программа для создания списка из длинны, верхнего и нижнего регистра
def string_info(string):
      count_calls()
      str_info = [len(string), string.upper(), string.lower()]
      return str_info
# Программа для проверки значения в списке
def  is_contains (string, list_to_search):
      count_calls()
      is_cont = string.upper() in [s.upper() for s in list_to_search]
      return is_cont
print(string_info('BaGdaSaRIAN'))
print(string_info('AleKSAndr'))
print(is_contains('PowDer', ['Pow', 'powder', 'der']))
print(is_contains('Phone', ['phonetic', 'mobile phone', 'fhonogram']))
print(calls)