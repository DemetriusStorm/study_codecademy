# Имя файла using_file.py

poem = '''
\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
'''
f = open('D:\\Temp\\poem.txt', 'w') # Открываем файла для записи
f.write(poem) # Записываем текст в файл
f.close() # Закрываем файл

f = open('D:\\Temp\\poem.txt')

while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')
f.close()

print()
new_poem = input('Пожалуйста, продолжите стих: ')
f2 = open('D:\\Temp\\poem.txt', 'a') # Открываем файла на дозапись 'a'
f2.write(new_poem) # Записываем текст в файл
f.close()
