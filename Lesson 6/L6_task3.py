# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'Доход с учетом премии составляет: {self._income["wage"] + self._income["bonus"]}\n')


employee1 = Position('Petr', 'Kuznetsov', 'Engineer', 30000, 10000)
print(employee1.name, employee1.surname, employee1.position, employee1._income)
employee1.get_full_name()
employee1.get_total_income()

employee2 = Position('Evgeny', 'Ivanov', 'Counselor', 40000, 15000)
print(employee2.name, employee2.surname, employee2.position, employee2._income)
employee2.get_full_name()
employee2.get_total_income()
