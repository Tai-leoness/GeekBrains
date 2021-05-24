# Реализовать структуру данных «Товары». Она должна представлять
# собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена,
# количество, единица измерения). Структуру нужно сформировать
# программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {“название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]}

goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'ед.': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'ед.': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Чтобы продолжить нажмите 'Enter', для вывода аналитики о товарах нажмите 'A': ").upper()
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите "{f}" ')
        features[f] = int(feature_) if (f == 'Цена' or f == 'Количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))



