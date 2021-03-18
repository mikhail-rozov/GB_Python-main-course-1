# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text_6.txt', encoding='utf-8') as f:     # Файл text_6.txt взят из предложенного примера и не
    my_list = f.readlines()                         # приложен к данной домашней работе

my_dict = {}

for el in my_list:
    el = el.split(':')
    for letter in el[1]:
        if not letter.isdigit():
            el[1] = el[1].replace(letter, ' ')
    el[1] = el[1].split()
    el[1] = [int(number) for number in el[1]]
    my_dict.update({el[0]: sum(el[1])})

print(my_dict)
