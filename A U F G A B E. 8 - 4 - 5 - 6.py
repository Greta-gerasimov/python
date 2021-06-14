#мне не вполне понятным видимо оказалась суть задания.

class Store():
    def __init__(self, *args):
        self.list_of_OfficeEquipment = []

    def input_(self):
        self.list_of_OfficeEquipment = input("введите количество принтеров:")
        print(f"мне нужно собрать {self.list_of_OfficeEquipment} принтеров")


class Office_equipment:
    def __init__(self, name, quantity, quality, cost):
        self.name = name
        self.quantity = quantity
        self.quality = quality
        self.cost = cost


    def __str__(self):
        return f'{self.name} цена {self.cost} количество {self.quantity}, назначение {self.quality}, цена {self.cost}'


class Printer(Office_equipment):
    def __init__(self, name, quantity, quality, cost, color):
        super().__init__(name, quantity, quality, cost)
        self.color = color
        if color == "BLACK":
            print(f"once you {color},always {color}")
        else:
            print(f"разноцветное мороженое вредно для детей и их будущего")


class Xerox(Office_equipment):
    def __init__(self, name, quantity, quality, cost, squarishes):
        super().__init__(name, quantity, quality, cost)
        self.squarishes = squarishes
        print(f'xerox {self.name} is {self.squarishes}')

@property
def cost(self):
    return self.__cost
@cost.setter
def cost(self, cost):
    if cost < 70:
        self.__cost = 70
    elif cost > 60:
        self.__cost = 60
    else:
        self.__cost = cost
def get_xerox_cost(self):
    return f"копировальная машина {self.name} стоит {str(self.cost)}"


Hp = Printer("Hp","345", "middle", "25", "BLACK")
canon = Printer("Canon","7888", "superior","35","Color")
xerox_ = Xerox("Xerox", "44444", "high", "67", "squarishes")
my_store = Store()
print(my_store.input_())
print(xerox_.get_xerox_cost())

#почему_то на выводе выходит None в какой-то момент, не понятно в ответ на что
#сеттер не работает. не понятно, как его вносить(в уже существующий список аттрибутивов)