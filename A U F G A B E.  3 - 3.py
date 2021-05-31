#oh , my Glob!

#3.
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def sum_Grob_Gob_Glob(x, y, z):
   total = []
   max1 = max(x, y, z)
   total.append(max1)
   max2 = (x + y + z) - max1 - min(x, y, z)
   total.append(max2)
   total_sum = sum(total)
   return total_sum

my = sum_Grob_Gob_Glob(3, 4, 5)
print(my)

#но потом я узнала про волшебную функцию remove.

def sum_Grob_Gob_Glob(x, y, z):
    seq = [x, y, z]
    seq.remove(min((x, y, z)))
    return sum(seq)

my = sum_Grob_Gob_Glob(3, 4, 5)
print(my)