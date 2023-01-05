# Ввести с клавиатуры целое число n.
#
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
#
# Использовать цикл for

value_input = int(input("Введіть ціле невід'ємне число: "))
value_counter = [i for i in range(1, (value_input + 1))]
result = 0

for item in value_counter:
    if item % 3 == 0:
        continue
    result += item ** 3
else:
    print('Сума кубів усіх чисел. Окрім чисел, кратних трьом: ', result)
