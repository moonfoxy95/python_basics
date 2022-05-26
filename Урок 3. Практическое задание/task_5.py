"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def summing_line(numbers):
    numbers = numbers.split(' ')
    summing = []
    for number in numbers:
        if number == 'q':
            return sum(summing)
        else:
            summing.append(int(number))
    return sum(summing)


global_summing = 0

while True:
    user_input = input("\nВведите 'q' вместо числа для выхода.\nВведите числа через пробел: ")
    result = summing_line(user_input)
    global_summing += result
    print(global_summing)
    if 'q' in user_input:
        break
