number = 23
guess = int(input('Введите целое число : '))
ask_yes = 'yes'
ask_no = 'no'

if guess == number:
    print('Вы угадали,')
    print('(хотя и не выиграли ни какого приза! До свидания)')
elif guess < number:
    print('Нет, загадочное число немного больше этого.')
else:
    print('Нет, загадочное число немного меньше этого.')
print('Завершено.')