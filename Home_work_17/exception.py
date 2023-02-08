# Создать программу-калькулятор в виде класса и несколько методов, как минимум сложение, вычитание,
# деление, умножение, возведение в степень и извлечение квадратного корня.
#
# Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.

class DegExcept(Exception):
    pass


class Calculator(object):

    def sum(self, x, y):
        try:
            res = x + y
            return res
        except ValueError:
            return 'Ви ввели не число, або не тільки число. Не треба так...'

    def minus(self, x, y):
        try:
            res = x - y
            return res
        except TypeError:
            return 'Ви ввели не число, або не тільки число. Не треба так...'

    def division(self, x, y):
        try:
            res = x / y
            return round(res, 3)
        except ZeroDivisionError:
            return 'О, ні, ви намагаєтеся поділити на нуль. Краще використати інше число!'
        except TypeError:
            return 'Ви ввели не число, або не тільки число. Не треба так...'

    def multi(self, x, y):
        try:
            res = int(x * y)
            return res
        except ValueError:
            return 'Перемножати можна тільки цифри...'
        except TypeError:
            return 'Напевно це не цифри'

    def deg(self, x, y):
        try:
            if y <= 0:
                raise DegExcept
            res = x ** y
            return res
        except TypeError:
            return 'Використовуйте тільки цифри!'
        except DegExcept:
            return 'Показник зведення у ступінь повинен бути більше 0'

    def root(self, x):
        try:
            res = x**0.5
            return round(res, 3)
        except TypeError:
            return 'Ви ввели від\'ємне значення або не число'


