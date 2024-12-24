# Создаем класс House с 2 атрибутами имененм и количеством этажей
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Создаем метод для приезда на этаж
    def go_to(self, new_floor):
        # Условие ограничения этажа приезда
        if 1 <= new_floor <= self.number_of_floors:
            # Цикл для перебора этажей с 1 до указанного (range исключает крайний объект конца, поэтому +1)
            for current_floor in range(1, new_floor + 1):
                # Выводим этаж после каждой итерации
                print(current_floor)
        else:
            print('Такого этажа не существует')

    # прописываем спец метод len и str
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    # прописываем спец методы арифметики
    def __eq__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print(f'невозможно сравнить, различные типы объектов ({type(self)} и {type(other)}')

    def __lt__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print(f'невозможно сравнить ({type(self)} и {type(other)}')

    def __le__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print(f'невозможно сравнить ({type(self)} и {type(other)}')

    def __gt__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print(f'невозможно сравнить ({type(self)} и {type(other)}')

    def __ge__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print(f'невозможно сравнить ({type(self)} и {type(other)}')

    def __ne__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print(f'невозможно сравнить ({type(self)} и {type(other)}')

    def __add__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            print(f'невозможно выполнить операцию объекты не соответствуют типам House и int')

    def __radd__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            return House.__add__(self, value)
        else:
            print(f'невозможно выполнить операцию объекты не соответствуют типам House и int')

    def __iadd__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            return House.__add__(self, value)
        else:
            print(f'невозможно выполнить операцию объекты не соответствуют типам House и int')

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
#
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# # __str__
# print(h1)
# print(h2)
# # __len__
# print(len(h1))
# print(len(h2))
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
