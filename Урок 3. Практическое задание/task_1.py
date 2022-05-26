"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def divide_number(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
    else:
        print(result)


try:
    number_1 = int(input("Введите делимое: "))
    number_2 = int(input("Введите делитель: "))
except ValueError:
    print("Введите число!")
else:
    divide_number(number_1, number_2)
