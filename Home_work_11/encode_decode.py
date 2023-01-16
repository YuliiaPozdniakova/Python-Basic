# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
#
# Декодировать её в строковый вид в кодировке по умолчанию.
#
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
#
# И на конец результат снова декодировать в строку.
#
# (результаты всех преобразований выводить на экран).

str_data = b'r\xc3\xa9sum\xc3\xa9'
print(str_data)
str_data_2 = str_data.decode()
print(str_data_2)

str_data_latin = str_data_2.encode("Latin1")
print(str_data_latin)
str_data_latin_2 = str_data_latin.decode("Latin1")
print(str_data_latin_2)

