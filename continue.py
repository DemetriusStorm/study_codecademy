# Имя файла continue.py

while True:
    s = input('Введите что-нибудь : ')
    if s == 'Выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введенная строка достаточной длины. Выходим?')
print('Вышли.')
    