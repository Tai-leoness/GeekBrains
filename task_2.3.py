# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_num = int(input("Введите номер месяца (от 1 до 12): "))
if 1 <= month_num <= 12:
    month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    seasons_list = ["Зима", "Осень", "Лето", "Весна"]
    if month_num == 1 or month_num == 12 or month_num == 2:
        print(month_dict.get(month_num))
        print(seasons_list[0])
    elif month_num == 3 or month_num == 4 or month_num == 5:
        print(month_dict.get(month_num))
        print(seasons_list[3])
    elif month_num == 6 or month_num == 7 or month_num == 8:
        print(month_dict.get(month_num))
        print(seasons_list[2])

    elif month_num == 9 or month_num == 10 or month_num == 11:
        print(month_dict.get(month_num))
        print(seasons_list[1])
else:
    print("Введите корректное число месяца - от 1 до 12!")