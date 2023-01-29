# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
#
# Продемонстрируйте их работу.

class Origami(object):
    paper_density = 80
    color_type = 'solid'
    ORIGAMI_NUMBER = 0
    DIFFICULT = None

    def __init__(self, min_age = 5):
        Origami.ORIGAMI_NUMBER += 1
        Origami.DIFFICULT = min_age
        self.min_age = min_age

    @staticmethod
    def make_method():
        return 'Make origami'

    @staticmethod
    def take_method():
        return 'Take it apart'

    @classmethod
    def origami_number(cls):
        return f'You make: {cls.ORIGAMI_NUMBER} origami'

    @classmethod
    def difficult(cls):
        return f'Уou succeeded in the task of difficulty: {cls.DIFFICULT}'


a = Origami()
b = Origami()

print(a.make_method())
print(a.take_method())
print(b.origami_number())
print(b.difficult())
