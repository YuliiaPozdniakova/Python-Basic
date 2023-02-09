# Создать генератор геометрической прогрессии


def GProgression_generator(value, denominator, lenght):
    counter = 1
    while counter <= lenght:
        yield value
        value *= denominator
        counter += 1


a = GProgression_generator(3, 4, 6)

try:
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration:
    pass

# або прокрутити в циклі

for i in a:
    print(i)
