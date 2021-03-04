# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.

income = int(input('Какая у компании выручка? '))
expenses = int(input('Какие у компании издержки? '))
rent = (income - expenses) / income

if income > expenses:
    print('Компания отработала с прибылью!')
    print(f'Рентабельность выручки составила {rent * 100:.1f}%')
    staff = int(input('Сколько сотрудников работает в компании? '))
    print(f'Прибыль в расчете на одного сотрудника составила: {(income - expenses) / staff:.1f}')
elif income == expenses:
    print('Выручка и издержки компании равны')
else:
    print('Компания отработала с убытком!')