# Созадать словарь в качестве ключа которого будет 6-ти значное число, а в качестве значений кортеж
# состоящий из 2-х элементов – имя(str), возраст(int). Сделать около 5-6 элементов словаря.
# записать данный словарь на диск в json-файл.
#
# data_dict = {x: {y: [i for i in range(i, i +2)] for y in 'XZY'} for x, i in zip('ABC', range(2))}
# print(data_dict)

import random
import json

name = ['Dave', 'Kristina', 'Rick', 'Karen', 'Frank', 'Becca']
age = [12, 23, 34, 45, 56, 67]

data_dict = {random.randint(100000, 999999): i for i in zip(name, age)}

with open('data_file.json', 'w') as write_dict:
    json.dump(data_dict, write_dict)
