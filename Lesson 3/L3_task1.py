# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(x, y):
    try:
        x = float(x)
        y = float(y)
        return round(x / y, 2)
    except ZeroDivisionError:
        return 'Деление на ноль!'
    except ValueError:
        return 'Ввести нужно числа!'


num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')

print(divide(num_1, num_2))
