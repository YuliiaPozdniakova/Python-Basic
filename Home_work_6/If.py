# Написать программу которая получит имя и возраст пользователя,
# проверяет возраст и выдаёт приветственное сообщение в зависимости от возраста:
#
# 	- меньше нуля или ноль или не число: “Ошибка, повторите ввод”;
#
# 	- больше нуля до 10 не включая: “Привет, шкет #Имя#”;
#
# 	- от 10 до 18 включая: “Как жизнь #Имя#?”
#
# 	- больше 18 и меньше 100: “Что желаете #Имя#?”
#
# 	- в противном случае: “#Имя#, вы лжете - в наше время столько не живут...”
#
# Программу необходимо завернуть в вечный цикл.
#
# После очередной отработки кода, спрашивать у пользователя "Желаете выйти? (Д/Y)".
# Если ответ будет буква "Д" или буква "Y" в любом регистре, то произвести выход из вечного цикла.
# В противном случае продолжить выполнение программы заново.


while True:
    user_name = input('Введите свое имя: ')
    user_age = input('Введите свой возраст: ')

    if not user_age.isdigit() or int(user_age) <= 0:
        print('Ошибка, повторите ввод')
    elif int(user_age) < 10:
        print('Привет, шкет, ' + user_name)   # або print(f'Привет, шкет, {user_name}')
    elif int(user_age) <= 18:
        print('Как жизнь, ' + user_name)    # або print(f'Как жизнь, {user_name}')
    elif int(user_age) < 100:
        print('Что желаете, ' + user_name)  # або print(f'Что желаете, {user_name}')
    else:
        print(user_name + ', вы лжете - в наше время столько не живут...')    #або print(f'{user_name}, вы лжете - в наше время столько не живут...')

    answer = input('Желаете выйти? (Д/Y) ')
    if answer.upper() in ('Y', 'Д'):
        break
