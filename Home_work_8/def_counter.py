# Дан список чисел.
#
# Посчитать сколько раз встречается каждое число.
# Использовать для подсчёта функцию.
#
# Подсказка: для хранения данных использовать словарь
# (ключ - само число, а значение - сколько раз оно встречается).
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.

import collections

lst = [3, 2, 1, 4, 2, 5, 3, 1, 2]

def count(a):
    return print(collections.Counter(lst))

count(lst)


