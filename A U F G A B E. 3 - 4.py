#вариант1 с использованием оператора возведения в степень

#4.
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def create_lemon_row(x, y):
    row_lemongrab = x ** y
    return row_lemongrab

x = float(input('ввести:'))
y = int(input('ввести:'))
print(create_lemon_row(x, y))

#вариант 2 с использованием цикла умножения числа самого на себя. у меня не получилось( отрицательная степень не работает
def create_lemon_row(x, y):
    res_lemon = 1
    for i in range(y):
       res_lemon *= x
    if y >= 0:
        return res_lemon
    else:
        return 1 / res_lemon


print(create_lemon_row(float(input('ввести число1:')), int(input('ввести число2:'))))