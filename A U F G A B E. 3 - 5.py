#5.
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

res = 0
def my_sum():
    while True:
        numbers = input('введите строку чисел или "$" для выхода:').split()
        for i in range(len(numbers)):
            try:
                if i == "$":
                    print(f'конечная сумма {res}. exit')
                    return
                else:
                    res += int(i)
                    print(f'конечная сумма{res}')

#вопрос по поводу преобразования строки в числа. нужно ли?
#код не работает(