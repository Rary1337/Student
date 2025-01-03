class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):\
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
         self.number_of_floors += value

    def __radd__(self, value):
        self.number_of_floors += value




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Название: ЖК Эльбрус', 10)
h4 = House('Название: ЖК Акация', 20)


h1.go_to(5)
h2.go_to(10)


print(h3)
print(h4)
print(len(h3))
print(len(h4))


print(h3 == h4)
print(h1 > h2)
print(h1 < h2)
print(h1 <= h4)
print(h3 >= h4)
print(h1 != h4)
print(len(h4))
h3.__add__(5)
print(len(h3))
h4.__radd__(7)
print(len(h4))