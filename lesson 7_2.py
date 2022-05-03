from abc import ABC, abstractmethod


class Clothes(ABC):
    total_its = 0
    total_exp = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.total_its += 1
        Clothes.total_exp += self.expense

    def __str__(self):
        return f'Пальто, размер - {self.size}, расход ткани - {self.expense} м.кв., '\
               f'общий расход ткани - {Clothes.total_exp:.02f} м.кв.'

    @property
    def expense(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Clothes.total_its += 1
        Clothes.total_exp += self.expense

    def __str__(self):
        return f'Костюм, для роста - {self.height}, расход ткани - {self.expense} м.кв., ' \
               f'общий расход ткани - {Clothes.total_exp:.02f} м.кв.'

    @property
    def expense(self):
        return round(self.height * 2 + 0.3, 2)


c1 = Coat(32)
print(c1)
c2 = Coat(30)
print(c2)
c3 = Suit(1.75)
print(c3)
c4 = Suit(1.90)
print(c4)