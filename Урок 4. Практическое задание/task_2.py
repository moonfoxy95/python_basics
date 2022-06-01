"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# С генератором
generator_list = [initial_list[i] for i in range(1, len(initial_list)) if initial_list[i] > initial_list[i-1]]
print(generator_list)

# Без генератора
non_generanor_list = []
for i in range(1, len(initial_list)):
    if initial_list[i] > initial_list[i-1]:
        non_generanor_list.append(initial_list[i])
print(non_generanor_list)
