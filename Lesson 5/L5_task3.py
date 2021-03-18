# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text_3.txt', 'r', encoding='utf-8') as f:    # Файл text_3.txt взят из предложенного примера и не
    the_list = f.readlines()                            # приложен к данной домашней работе

my_dict = {}

for el in the_list:
    el = el.replace('\n', '')
    el = el.split()
    my_dict.update({el[0]: float(el[1])})

low_salary = '\n'
total_salary = 0

for name, salary in my_dict.items():
    if salary < 20000:
        low_salary += f'{name}\n'
    total_salary += salary

print(f'Список сотрудников с окладом менее 20 тысяч:{low_salary}')
print(f'Средний оклад сотрудников составляет:\n{int(total_salary / len(my_dict))}')
