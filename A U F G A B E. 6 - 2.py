#Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():
    def __init__(self, leght, width,density, thickness):
        self._leght = leght
        self._width = width
        self.density = density
        self.thickness = thickness

    def mass(self):
        return self._leght * self._width * self.density * self.thickness



awesome_road = Road(20, 5000, 25, 5)
print(awesome_road.mass())








