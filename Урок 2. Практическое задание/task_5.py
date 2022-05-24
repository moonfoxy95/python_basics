"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""


def exercice_5():
    my_list = [7, 5, 3, 3, 2]
    print(my_list)
    while True:
        user_input = input("Введите число: ")

        # break if user_input == 'q' else pass
        if user_input == 'q':
            break

        user_input = int(user_input)
        if user_input in my_list:
            times_in_list = my_list.count(user_input)
            first_met = my_list.index(user_input)
            my_list.insert(first_met + times_in_list, user_input)
            print(my_list)
        else:
            my_list.append(user_input)
            my_list.sort()
            my_list.reverse()
            print(my_list)


exercice_5()
