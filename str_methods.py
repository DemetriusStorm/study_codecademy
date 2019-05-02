# Имя файла str_methods.py

name = 'Demetrius'

if name.startswith('Dem'):
    print('Да, строка начинается на "Dem"')
    
if 'i' in name:
    print('Да, она содержит строку "i"')
    
if name.find('ups') != -1: # find возвращает -1, если подстрока не обнаружена
    print('Да, она содержит строку "ups"')
    
delimiter = '|~*~|'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))