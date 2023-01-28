# Прочитать сохранённый json-файл из задания №18 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.

import json
import csv
import random

with open('data_file.json') as write_dict:
    output_data = json.load(write_dict)


name_of_fields = ['Person', 'Id', 'Name', 'Age', 'Phone']
fields = []

for item in output_data:
    value = output_data[item]
    value.insert(1, item)
    value.insert(0, 'Person')
    fields.append(value)

# додавати рядок персон і поряд його "номер". можливо використати функцію енумерейт і змінити точку відлику з 0 на 1
# змінити функцію генерації мобільних номерів на номери з реальними кодами операторів. Зробити обрання коду випадковим
# прописати додавання телефону в кінець списку. можливо використати екстенд

print(fields)

# with open('data_csv.csv', mode='w', encoding='utf-8') as write_file:
#     file_writer = csv.writer(write_file)
#     file_writer.writerow(name_of_fields)
#     for item in fields:
#         file_writer.writerow(item)

# phone_list = []
# while len(phone_list) < 10:
#     num = str(random.randint(0, 999999999)).zfill(9)
#     if not num in phone_list:
#         phone_list.append(num)
# # print(phone_list)
