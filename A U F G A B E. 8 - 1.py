#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


from datetime import *

class Date:
    def __init__(self, today):
        self.today = today
    def strftime(self, today):
        return today.strftime('%d-%m-%Y')
    def __str__(self):
        return f"current date is {Date(self, today)}"

    @classmethod
    def extract(cls, today):
        date_separate = []

        for i in today.split():
            if i != "-":
                date_separate.append(i)

        return int(date_separate[0]), int(date_separate[1]), int(date_separate[2])

    @staticmethod
    def get_valid(day, month, year):
        if 1 <= day <= 31:
            return f"Good"
        else:
            return f"BALDA"
        if 1 <= month <= 12:
            return f"Good"
        else:
            return f"BALDA"
        if year == 2021:
            return f"Good"
        else:
            return f"BALDA"


    def __str__(self):
        return f"current date is {Date(self, today)}"

today_is = Date('04-04-2019')
print(today_is)
print(Date.get_valid(34, 5, 1001))
print(Date.extract("13 - 6 - 2021"))
# doesn't work
#пыталась использовать форматирование даты, но как-то все неудачно вышло