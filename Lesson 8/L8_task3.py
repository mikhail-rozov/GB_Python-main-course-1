# Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать
# типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
# скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
# вносить его в список, только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа
# скрипта не должна завершаться.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


the_list = []

while True:
    try:
        number = input('Enter a number for adding to the list or type "stop" to see the result: ')
        if number.lower() == 'stop':
            break
        try:
            the_list.append(int(number))
        except ValueError:
            raise MyError('It is not a number! Try again.')
    except MyError as err:
        print(err)

print(the_list)
