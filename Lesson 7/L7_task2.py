# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, measure):
        self.measure = measure

    def __add__(self, other):
        return self.count_fabric + other.count_fabric

    @abstractmethod
    def count_fabric(self):
        pass


class Coat(Clothes):

    @property
    def count_fabric(self):
        return round(self.measure / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def count_fabric(self):
        return 2 * self.measure + 0.3


coat_1 = Coat(6)
suit_1 = Suit(4)

print(coat_1.count_fabric)
print(suit_1.count_fabric)
print(suit_1 + coat_1)
