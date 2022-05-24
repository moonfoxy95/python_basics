"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""


def exercise_1():
    my_list = [1, 'cat', 9.81, False, None, ['2', 3], (4, 'five'),
               {6, 6, 6, 7, 7}, {8: 'number eight', 9: 'number nine'},
               frozenset({'dog', 'fish', 44}), b'what a day',
               bytearray(b"very nice text")]
    for i, element in enumerate(my_list, 1):
        print(i, type(element))


exercise_1()
