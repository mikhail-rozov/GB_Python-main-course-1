# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input('Enter the dividend: '))
    b = int(input('Enter the divisor: '))
    if b == 0:
        raise MyError('Division by zero!')
except MyError as err:
    print(err)
except ValueError:
    print('Should be numbers!')
else:
    print(f'The result is: {a / b}')
