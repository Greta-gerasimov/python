#Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка


from functools import reduce

data = [i for i in range(100, 1001) if i % 2 == 0]
def multiply(first, second):
    return first * second

result = reduce(multiply, data)

print(result)



