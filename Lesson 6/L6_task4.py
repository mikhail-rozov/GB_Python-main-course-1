# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def get_info(self):
        print(f'\nSpeed: {self.speed}, Color: {self.color}, Name: {self.name}, Belongs to police: {self.is_police}')

    def go(self):
        print('The car started moving!')

    def stop(self):
        print('The car stopped!')

    def turn(self, direction):
        print(f'The car turned {direction}!')

    def show_speed(self):
        print(f'The car is moving {self.speed} kilometers per hour!')


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f'The speed limit is exceeded!')


class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f'The speed limit is exceeded!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


a = TownCar(75, 'Yellow', 'Hyundai')
a.get_info()
a.go()
a.show_speed()
a.turn('Right')
a.stop()

b = WorkCar(50, 'Brown', 'Mercedes')
b.get_info()
b.go()
b.show_speed()
b.turn('Left')
b.stop()

c = SportCar(100, 'Red', 'Porsche')
c.get_info()
c.go()
c.show_speed()
c.stop()

d = PoliceCar(80, 'White', 'Ford')
d.get_info()
d.go()
d.show_speed()
d.stop()
