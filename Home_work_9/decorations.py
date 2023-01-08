# Написать декоратор к 2-м любым функциям,
# который бы считал и выводил время их выполнения.
#
# Подсказка:
#
# from datetime import datetime
#
# time = datetime.now()

from datetime import datetime


def time_deckor(func):
    def wrapper():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print('Час виконання функції: ', end_time - start_time)

    return wrapper


@time_deckor
def function_1():
    print('wow, your amazing!')


@time_deckor
def function_2():
    a = 10 + (5**3)
    print('a = ', a)


function_1()
function_2()
