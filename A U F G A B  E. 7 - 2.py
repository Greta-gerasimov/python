#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды
# использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Garment:
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    def fabric_consumption_coat(self):
        return self.size / 6.5 + 0.5

    def fabric_consumption_suit(self):
        return self.height * 2 + 0.5

    @property
    def fabric_consumption_full(self):
        return self.fabric_consumption_full

    @fabric_consumption_full.setter
    def fabric_consumption_full(self, fabric_consumption_coat, fabric_consumption_suit):
        return f'fabric consumption of garment is {str((self.size / 6.5 + 0.5) + (self.height * 2 + 0.5))}'


class Coat(Garment):
    def __init__(self, name, size, height):
        super().__init__(name, size, height)

    def fabric_consumption_coat(self):
        Garment.fabric_consumption_coat(self)

    def fabric_consumption_full(self):
        Garment.fabric_consumption_full(self)


class Suit(Garment):
    def __init__(self,name, size, height):
        super().__init__(name, size, height)

    def fabric_consumption_suit(self):
        Garment.fabric_consumption_suit(self)

    def fabric_consumption_full(self):
        print('fabric consumption_full() of suit')
        Garment.fabric_consumption_full(self)


c = Coat('uniquefabrique', 7, 8)
s = Suit('sudar', 9, 11)
print(c.__dict__)
print(s.__dict__)
print(c.fabric_consumption_full())
print(s.fabric_consumption_full())
print(c.fabric_consumption_coat())
print(s.fabric_consumption_suit())

#выдает ошибку. не вполне ясно.