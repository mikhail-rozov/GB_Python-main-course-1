# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между
# режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

import time
import turtle


class TrafficLight:

    __color = 'red'

    # # Метод без использования графики:
    #
    # def running(self):
    #     print(f'{self.__color.capitalize()}!')
    #     while True:
    #         if self.__color == 'red':
    #             time.sleep(7)
    #             self.__color = 'yellow'
    #             print('Yellow!')
    #         elif self.__color == 'yellow':
    #             time.sleep(2)
    #             self.__color = 'green'
    #             print('Green!')
    #         elif self.__color == 'green':
    #             time.sleep(10)
    #             self.__color = 'red'
    #             print('Red!')

    def draw_circle(self, color):
        turtle.color(color)
        turtle.begin_fill()
        turtle.delay(0)
        turtle.circle(100)
        turtle.end_fill()

    def running(self):
        while True:
            if self.__color == 'red':
                self.draw_circle(self.__color)
                time.sleep(7)
                self.__color = 'yellow'
                continue
            elif self.__color == 'yellow':
                self.draw_circle(self.__color)
                time.sleep(2)
                self.__color = 'green'
                continue
            elif self.__color == 'green':
                self.draw_circle(self.__color)
                time.sleep(10)
                self.__color = 'red'
                continue


traffic_light1 = TrafficLight()
try:
    traffic_light1.running()
except turtle.Terminator:
    print('Работа программы завершена.')
