# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.

my_list = ['string', 32, 2.42, (2, 'sde'), {False, 3.44}, [53, 5.75], {23: 'fffd', 'dde': 4.33}, print]

for i in my_list:
    print(type(i))
