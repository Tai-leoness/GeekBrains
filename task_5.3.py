# Создать текстовый файл (не программно), построчно
# записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад
# менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

firm = dict(Иванов=17000, Петров=21000, Сидоров=19000, Гагарин=20050)
try:
    file_obj = open("test_5.3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_5.3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Оклад менее 20к : {persons}")
print(f"Доход в среднем: {result}")