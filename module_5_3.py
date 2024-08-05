class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors > new_floor > 1:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print("Такого этажа не существует")

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __add__(self, other):
        self.number_of_floors += other
        return self


House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)
House_3 = House('ТК "Северный"', 4)

House_1.go_to(5)
House_2.go_to(10)
House_3.go_to(3)

print(str(House_1))
print(str(House_2))
print(str(House_3))

print(len(House_1))
print(len(House_2))
print(len(House_3))

print(House_1)
print(House_2)
print(House_3)

print(House_1 == House_3)

House_3 = House_3 + 14
print(House_3)
print(House_3 == House_1)

House_1 += 3
print(House_1)

House_2 = House_2 + 1
print(House_2)

print(House_1 < House_3)
print(House_2 <= House_1)
print(House_1 != House_2)
print(House_1 > House_3)
print(House_1 >= House_2)
