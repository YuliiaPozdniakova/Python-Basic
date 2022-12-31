# Ввести с клавиатуры целое число n.
#
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
#
# Использовать цикл while


input_value = int(input('Введіть ціле число: '))
counter = 1
result = 1

while input_value > counter:
    counter += 1
    if counter %3 == 0:
        continue
    result += counter**3

print('Сума кубів усіх чисел. Окрім чисел, кратних трьом: ', result)

