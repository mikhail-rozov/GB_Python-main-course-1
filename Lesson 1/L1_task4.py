# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
max_number = 0
last_number = 0

while True:
    if number // 10 == 0:
        last_number = number
        if last_number > max_number:
            max_number = last_number
        break
    else:
        last_number = number % 10
        number = (number - last_number) // 10
    if last_number > max_number:
        max_number = last_number

print(f' Самая большая цифра в данном числе: {max_number}')
