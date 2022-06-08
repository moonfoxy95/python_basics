"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.mass_for_meter = 25
        self.thickness = 0.05

    def calculation(self):
        result = self._lenght * self._width * self.mass_for_meter * self.thickness
        print(f"{self._lenght}м*{self._width}м*{self.mass_for_meter}кг*{self.thickness}м = {result:.0f}кг = {result/1000:.0f}т.")

a = Road(20, 5000)
a.calculation()
