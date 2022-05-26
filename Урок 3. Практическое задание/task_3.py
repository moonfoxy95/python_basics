"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_1(a, b, c):
    numbers = [a, b, c]
    numbers.sort(reverse=True)
    highest = numbers[0]
    second_highest = numbers[1]
    print(highest + second_highest)


def my_func_2(a, b, c):
    numbers = [a, b, c]
    highest = None
    second_highest = None

    while second_highest is None:
        if numbers[0] > numbers[1]:
            if highest is None:
                highest = numbers.pop(0)
            else:
                second_highest = numbers.pop(0)
        else:
            if highest is None:
                highest = numbers.pop(1)
            else:
                second_highest = numbers.pop(1)

    if highest > second_highest:
        pass
    else:
        highest, second_highest = second_highest, highest

    print(highest + second_highest)


my_func_1(1, 14, 6)
my_func_2(1, 14, 6)
