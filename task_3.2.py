# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input("Введите имя ")
surname = input("Введите фамилию ")
year = input("Год рождения ")
city = input("Город ")
email = input("Электроннаую почту ")
phone = input("Номер телефона ")
def my_func(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])
print(my_func(name, surname, year, city, email, phone))
