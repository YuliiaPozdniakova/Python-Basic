# Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей,
# вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.

import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'(radius={self.radius}, ' + super().__str__()[1:]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        if self.radius == other.radius:
            return Point(x, y)
        else:
            radius = self.radius - other.radius
            return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)


a = Circle(1, 4, 4)
b = Circle(1, 2, 2)

c = a - b
print(c)
