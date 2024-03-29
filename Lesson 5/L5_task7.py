# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
# прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
# словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json


my_dict = {}
company_count = 0
total_profit = 0

with open('text_7.txt', encoding='utf-8') as f:     # Файл text_7.txt взят из предложенного примера и не
    for line in f:                                  # приложен к данной домашней работе
        line = line.replace('\n', '')
        line = line.split()
        profit = int(line[2]) - int(line[3])
        my_dict.update({line[0]: profit})
        if profit > 0:
            total_profit += profit
            company_count += 1

profit_dict = {'average_profit': int(total_profit / company_count)}

the_list = [my_dict, profit_dict]
print(the_list)

with open('text_7.json', 'w', encoding='utf-8') as f:
    json.dump(the_list, f, indent=4, ensure_ascii=False)
