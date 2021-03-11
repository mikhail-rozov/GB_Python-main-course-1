# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    try:
        x, y, z = float(x), float(y), float(z)
        result = [x, y, z]
        result.sort(reverse=True)
        result = result[0] + result[1]
        return result
    except ValueError:
        return 'Нужно ввести числа!'


num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')
num_3 = input('Введите третье число: ')

print(my_func(num_1, num_2, num_3))
