# Сделать программу в виде функции в которой нужно будет угадывать число.


import random


def guess_the_number():
    while True:
        input_int = int(input('Вгадайте число від 1 до 3: '))
        random_int = random.randint(1, 3)
        if input_int == random_int:
            print('Ви вгадали!')
            break
        else:
            print('Ви не вгадали :( Спробуйте ще!')


guess_the_number()

# або трохи розширена версія


def guess_the_number():
    while True:
        input_int = int(input('Вгадайте число від 1 до 3: '))
        random_int = random.randint(1, 3)
        if input_int == random_int:
            print('Ви вгадали!')
            answer = input('Хочете вийти (натисність: N) чи продовжити (натисніть: Y) ? ')
            if answer.upper() in ('N'):
                break
            elif answer.upper() in ('Y'):
                continue
        else:
            print('Ви не вгадали :( Спробуйте ще!')


guess_the_number()
