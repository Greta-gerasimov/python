#1.
# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
def div_Grob_Gob(x, y):
    try:
        div = x / y
    except ZeroDivisionError:
        return 'BALDA'

    return div


x = int(input('ввести'))
y = int(input('вdести'))

dv_gob = div_Grob_Gob(x, y)
print(dv_gob)