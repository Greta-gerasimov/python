#Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name}  turn right'

    def turn_left(self):
        return f'{self.name}  turn left'

    def show_speed(self):
        return f'speed of {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self,speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'speed of TownCar {self.name} is {self.speed}')

        if self.speed > 60:
            return f'speed limit is 60'
        else:
            return f'speed of TownCar {self.name} is ok'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

        def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)

        def show_speed(self):
            print(f'speed of Woekcar {self.name} is {self.speed}')

            if self.speed > 60:
                return f'speed limit is 40'
            else:
                return f'speed of WorkCar {self.name} is ok'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

volvo = TownCar(90, 'Red', 'Volvo', False)
tesla = SportCar(130, 'Yellow', 'Tesla', False)
batmobilie = WorkCar(300,'Black', 'I_AM_BATMAN', False)
dodge = PoliceCar(150, 'Black', 'GET_OUT', True)

print(tesla.__dict__)
volvo.show_speed()
print(f'tesla.go() with sleed {tesla.show_speed()}')
print(dodge.turn_left())