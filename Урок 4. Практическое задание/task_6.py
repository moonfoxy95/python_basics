"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

first_number = int(input('Input first number: '))
last_number = int(input('Input last number: '))

for number in count(first_number):
    if number > last_number:
        break
    print(number, end=' ')


input_list = [input('Input words (divided by space): ').split()]
repeats = int(input('Repeats: '))

i = 0
for word in cycle(input_list):
    i += 1
    if i > repeats:
        break
    print(word, end=' ')
