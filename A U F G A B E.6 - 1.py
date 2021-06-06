#Создать класс TrafficLight (светофор) и определить у него один
# #атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import *

class TrafficLight:
    def __init__(self, color):
        self._color = color

    color_changes = ['red', 'yellow', 'green']

    def running(self):
        print('traffic light is activated')

    i = 0
    while i < 3:
        print(f'traffic light switches to \n'
              f'{color_changes[i]}')

        if i == 0:
            sleep(7)
        elif i == 1:
            sleep(2)
        elif i == 2:
            sleep(5)
            i += 1

signal = TrafficLight()
TrafficLight.running()





