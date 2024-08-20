class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        print(isinstance(other, House))
        if isinstance(other, House):
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
        print(isinstance(other, int))
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other


House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)
House_3 = House('ТК "Северный"', 4)

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

House_2 = 10 + House_2
print(House_2)

print(House_1 < House_3)
print(House_2 <= House_1)
print(House_1 != House_2)
print(House_1 > House_3)
print(House_1 >= House_2)
