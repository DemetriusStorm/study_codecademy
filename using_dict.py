# Имя файла using_dict.py

adr_book = { 'Demetrius' : 'eof@rambler.ru',
             'Aleksey' : 'iamsol@ya.ru',
             'NoName' : 'china@noname.ch'
}

print('Почта Дмитрия:', adr_book['Demetrius'])
#print('Вся адресная книга:', adr_book)

# Удаление пары ключ:значение
del adr_book['NoName']
print('\nВ адресной книге {0} контактов\n'.format(len(adr_book)))

for name, address in adr_book.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
    
# Добавляем пару ключ:значение
adr_book['HzKto'] = 'hzkto@hzgde.hz'
if 'HzKto' in adr_book:
    print("\nАдрес HzKto:", adr_book['HzKto'])

print('\nВ адресной книге {0} контактов\n'.format(len(adr_book)))
for name, address in adr_book.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
    