# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
#
# Создать файл и записать в него первые 2 строки и закрыть файл.
#
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
#
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

input_data_1 = input('Введіть рядок 1: ')
input_data_2 = input('Введіть рядок 2: ')
input_data_3 = input('Введіть рядок 3: ')
input_data_4 = input('Введіть рядок 4: ')

item_1 = [input_data_1 + '\n', input_data_2 + '\n']
item_2 = [input_data_3 + '\n', input_data_4 + '\n']

with open('text_file.txt', 'w') as input_write:
    input_write.writelines(item_1)

with open('text_file.txt', 'a') as input_write:
    input_write.writelines(item_2)
