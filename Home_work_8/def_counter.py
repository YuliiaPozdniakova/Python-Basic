# Дан список чисел.
#
# Посчитать сколько раз встречается каждое число.
# Использовать для подсчёта функцию.
#
# Подсказка: для хранения данных использовать словарь
# (ключ - само число, а значение - сколько раз оно встречается).
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.


list_number = [3, 2, 1, 4, 2, 5, 3, 1, 2]
dict_result = {}


def count_number(list_number, dict_result):
    for i in list_number:
        if i in dict_result:
            dict_result[i] += 1
        else:
            dict_result[i] = 1
    print(dict_result)


count_number(list_number, dict_result)


# інше рішення, яке було першим.
# але мені здалося, що воно не дуже гарне в контексті умов завдання
#
# import collections
#
# def count(a):
#     return print(collections.Counter(lst))
#
# count(list_number)


