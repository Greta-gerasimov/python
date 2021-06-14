#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivisionByZero:
    """I always end up dividing by zero!!!"""

    def __init__(self, devisor, denominator):
        self.devisor = devisor
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(devisor, denominator):
         try:
             return(devisor/denominator)
         except:
             return(f'division be zero')

division_=DivisionByZero(29,0)
print(division_.divide_by_zero(29,0))
print(DivisionByZero.divide_by_zero(3,20))
print(DivisionByZero.divide_by_zero(3,0))
