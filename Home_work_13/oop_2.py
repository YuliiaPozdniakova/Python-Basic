# Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.
#
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention»,
# его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
#
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.
#
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.

import time

class Auto(object):
    brand = None
    age = 0
    color = 'black/white'
    mark = None
    weight = 1000

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        print(self.age + 1)


class Truck(Auto):

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.__max_speed = max_speed

    def move(self):
        super().move()
        print('max speed is', self.__max_speed)


iveco_truck = Truck('Iveco', 2, 'Daily', 7.5)
# iveco_truck.color = 'red' - можна перепризначити колір за замовчуванням
# iveco_truck.weight = 8000 - можна перепризначити вагу за замовчуванням
print('brand: ', iveco_truck.brand)
print('age, year: ', iveco_truck.age)
print('color: ', iveco_truck.color)
print('mark: ', iveco_truck.mark)
print('weight, kg: ', iveco_truck.weight)
print('max. load, m: ', iveco_truck.max_load)
iveco_truck.stop()
iveco_truck.birthday()
iveco_truck.move()
iveco_truck.load()

print('-' * 50)

man_truck = Truck('MAN', 5, 'TGX', 5.805)
# man_truck.color = 'orange' # можна перепризначити колір за замовчуванням
# man_truck.weight = 7000 # можна перепризначити вагу за замовчуванням
print('brand: ', man_truck.brand)
print('age, year: ', man_truck.age)
print('color: ', man_truck.color)
print('mark: ', man_truck.mark)
print('weight, kg: ', man_truck.weight)
print('max. load, m: ', man_truck.max_load)
man_truck.stop()
man_truck.birthday()
man_truck.move()
man_truck.load()

print('-' * 50)

bmw_car = Car('BMW', 1, 'BMW M', 309)
# bmw_car.color = 'grey' # можна перепризначити колір за замовчуванням
# bmw_car.weight = 2000 # можна перепризначити вагу за замовчуванням
print('brand: ', bmw_car.brand)
print('age, year: ', bmw_car.age)
print('color: ', bmw_car.color)
print('mark: ', bmw_car.mark)
print('weight, kg: ', bmw_car.weight)
bmw_car.stop()
bmw_car.birthday()
bmw_car.move()

print('-' * 50)

audi_car = Car('Audi', 3, 'Q8', 240)
# audi_car.color = 'green' # можна перепризначити колір за замовчуванням
# audi_car.weight = 1500 # можна перепризначити вагу за замовчуванням
print('brand: ', audi_car.brand)
print('age, year: ', audi_car.age)
print('color: ', audi_car.color)
print('mark: ', audi_car.mark)
print('weight, kg: ', audi_car.weight)
audi_car.stop()
audi_car.birthday()
audi_car.move()