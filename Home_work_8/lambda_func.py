# Написать лямбда-функцию определяющую чётное/нечётное.
#
# Функция принимает параметр (число) и если чётное,
# то выдаёт слово “чётное”, если нет - то “не чётное”.

input_value = int(input("Введіть ціле невід'ємне число: "))

fnc = lambda a: 'парне' if (a % 2 == 0) else 'непарне'
print(fnc(input_value))


