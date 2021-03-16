# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys


def calc_salary(work_time, salary_per_hour, bonus):
    work_time, salary_per_hour, bonus = int(work_time), int(salary_per_hour), int(bonus)
    return work_time * salary_per_hour + bonus


try:
    salary = calc_salary(sys.argv[1], sys.argv[2], sys.argv[3])
    print(f"Employee's salary: {salary}")
except ValueError:
    print('The parameters have to be numbers!')
