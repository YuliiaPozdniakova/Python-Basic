# Ввести с клавиатуры целое число n.
#
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
#
# Использовать цикл for

value_input = int(input("Введіть ціле невід'ємне число: "))
value_counter = [i for i in range(1, (value_input + 1))]
result = [i**3 for i in value_counter]
print(result)

# for value in value_input:
