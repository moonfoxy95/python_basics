"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction='направо'):
        print(f"Машина повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} км/ч.")
# TownCar, SportCar, WorkCar, PoliceCar


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed-60} км/ч!")
        else:
            print(f"Текущая скорость автомобиля: {self.speed} км/ч.")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed-40} км/ч!")
        else:
            print(f"Текущая скорость автомобиля: {self.speed} км/ч.")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lada = TownCar(86, 'красный', 'жигули', False)
bmw = SportCar(130, 'черный', 'БМВ', False)
gazel = WorkCar(74, 'белый', 'газель', False)
mustang = PoliceCar(55, 'бело-синий', 'мустанг', True)

lada.go()
bmw.stop()
gazel.turn('налево')
mustang.show_speed()

lada.show_speed()
gazel.show_speed()
