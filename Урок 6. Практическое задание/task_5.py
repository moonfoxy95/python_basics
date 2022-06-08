"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f"{self.title} пишет.")


class Pencil(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f"{self.title} рисует.")


class Handle(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f"{self.title} маркирует.")


a = Stationery('канцелярская принадлежность')
b = Pen('ручка')
c = Pencil('карандаш')
d = Handle('маркер')

a.draw()
b.draw()
c.draw()
d.draw()
