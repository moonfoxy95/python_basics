"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv
script_name, hours_worked, salary_per_hour, bonus = argv
salary = int(hours_worked) * int(salary_per_hour) + int(bonus)
print(salary)
