number = 23
running = True

while running:
    guess = int(input('Введите целое число : '))
    
    if guess == number:
        print('Точно!')
        running = False
    elif guess < number:
        print('Нет, число больше')
    else:
        print('Нет, число меньше')
else:
    print('Цикл while закончен.')
print('Завершение.')