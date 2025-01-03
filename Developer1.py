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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Название: ЖК Эльбрус, Количество этажей: 10', 10)
h4 = House('Название: ЖК Акация, Количество этажей: 20', 20)

h1.go_to(5)
h2.go_to(10)


print(h3)
print(h4)
print(len(h3))
print(len(h4))