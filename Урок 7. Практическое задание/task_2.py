"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def get_coat_material_usage(self):
        pass

    @abstractmethod
    def get_costume_material_usage(self):
        pass

    def get_total_material_usage(self):
        pass


class Clothes(AbstractClothes):
    # Coat, Costume
    def __init__(self, size = 0, height = 0):
        self.size = size
        self.height = height
        self.coat_material_usage = self.size / 6.5 + 0.5
        self.costume_material_usage = 2*self.height + 0.3


    def get_coat_material_usage(self):
        return f"Расход ткани на пальто: {self.coat_material_usage:.2f}"

    def get_costume_material_usage(self):
        return f"Расход ткани на костюм: {self.costume_material_usage:.2f}"

    @property
    def get_total_material_usage(self):
        result = self.coat_material_usage + self.costume_material_usage
        return f'Общий расход ткани: {result:.2f}'

c = Clothes(5, 10)
print(c.get_coat_material_usage())
print(c.get_costume_material_usage())
print(c.get_total_material_usage)

