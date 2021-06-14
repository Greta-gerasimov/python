#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean

with open('again.txt', 'r') as payroll_file:
    sal = []
    poor = []
    payroll_list = payroll_file.read().split('\n')
    for i in payroll_list:
       i == i.split()
    if int(i[1]) < 20:
        poor.append(i[0])
    sal.append(i[1])

print(f'poor is {poor}', mean(sal))


