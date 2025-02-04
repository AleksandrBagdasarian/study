class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def __repr__(self):
        return f"{self.name}"

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(F"{self.name} не стал есть {food.name}")
            self.alive = False
        return

class Plant:
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible

    def __repr__(self):
        return f"{self.name}"

class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name, edible=True):
        super().__init__(name, edible)

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


