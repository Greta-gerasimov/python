# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    with open ('aufgabe 5-5.txt', 'w+') as file_obj:
        line = input('введите числа через пробел')
        file_obj.writelines(line)
        numbers_ = line.split()

        print(sum(map(int, numbers_)))

summary()