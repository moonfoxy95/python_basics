"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""


from functools import reduce

my_list = reduce(lambda a, b: a * b, [number for number in range(100, 1001) if number % 2 == 0])
print(my_list)
