# Дан словарь, создать новый словарь при помощи конструкции
# генератор словаря, поменяв местами ключ и значение.

dict_old = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}

dict_new = {value: key for key, value in dict_old.items()}

print(dict_new)
