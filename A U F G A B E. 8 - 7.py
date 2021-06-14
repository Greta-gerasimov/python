#Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __str__(self):
        return f'z {self.x} + ({self.y} * i)'

    def __add__(self, other):
        return f'z = {self.x + other.x}  + {self.y + other.y}'

    def __mul__(self, other):
        return f'z = ({self.x * other.x} - {self.y * other.y}) + {self.y * other.y} * i'



z_1 = Complex(1, 8)
z_2 = Complex(4, 7)
print(z_1)
print(z_1 * z_2)
print(z_2 + z_1)
