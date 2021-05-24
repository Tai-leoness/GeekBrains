# Создать список и заполнить его элементами различных типов данных.
# #Реализовать скрипт проверки типа данных каждого элемента. #
# Использовать функцию type() для проверки типа.
# #Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

this_str = "Hi, Alexandra"
this_int = 9
this_tuple = ('y', '9')
this_list = ['x', '333']
this_float = 1.2
this_dict = {'city': 'Hurghada', 'country': 'Egypt'}
all_types = [this_str, this_int, this_tuple, this_list, this_float, this_dict]
for i in all_types:
    print(f'{i} is {type(i)}')