# Программа принимает действительное положительное число x и
# целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.

def my_func(x, y):
    return x ** y
print(my_func(int(input("Введите действительное положительное x ")), int(input("Введите целое отрицательное число y "))))