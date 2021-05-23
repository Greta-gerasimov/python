задание 3.
#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень).
# Напишите решения через list и через dict.
n = int(input())
season_list = ["winter", "spring", "autumn", "summer"]
season_dict = {1: 'winter',
               2: 'spring',
               3: 'autumn',
               4: 'summer'}
if n == 12 or n == 1 or n == 2:
    print(season_list[0])
    print(season_dict.get(1))
elif n == 3 or n == 4 or n == 5:
    print(season_list[1])
    print(season_dict.get(2))
elif n == 6 or n == 7 or n == 8:
    print(season_list[3])
    print(season_dict.get(4))
elif n == 9 or n == 10 or n == 11:
    print(season_list[2])
    print(season_dict.get(3))
else:
    none
