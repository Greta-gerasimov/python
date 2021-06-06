# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'запуск отрисовки'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} is activated. запуск отрисовки'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} is activated. запуск отрисовки'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} is activated. запуск отрисовки'

parker = Pen ('Parker')
koh_i_noor = Pencil('Koh_i_noor')
stabilo = Handle('Stabilo')
print(parker.__dict__)
print(koh_i_noor.draw())
print(parker.draw())
print(stabilo.draw())

