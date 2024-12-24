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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)