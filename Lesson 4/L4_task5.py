# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import functools as ft


def multiply(a, b):
    return a * b


the_list = [number for number in range(100, 1001) if number % 2 == 0]

result = ft.reduce(multiply, the_list)
print(result)
