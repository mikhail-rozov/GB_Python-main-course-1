# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
# с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их
# тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return str(Date.extract_date(self.date))

    @classmethod
    def extract_date(cls, date):
        date = date.split('-')
        day, month, year = int(date[0]), int(date[1]), int(date[2])
        return day, month, year

    @staticmethod
    def validate(date):
        date = date.split('-')
        if int(date[0]) > 31 or int(date[0]) < 1 or len(date[0]) != 2:
            raise ValueError
        if int(date[1]) > 12 or int(date[1]) < 1 or len(date[1]) != 2:
            raise ValueError
        if len(date[2]) != 4:
            raise ValueError


try:
    date_1 = Date(input('Enter a date in dd-mm-yyyy format: '))
    Date.validate(date_1.date)
    print(date_1)
except ValueError:
    print('Wrong date format!')
