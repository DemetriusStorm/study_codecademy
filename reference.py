# Имя файла reference.py

print('Простое присваивание')
shoplist = ['яблоки', 'молоко', 'хлеб', 'мука', 'соль']
mylist = shoplist # mylist - лишь еще одно имя, указывающее на тот же объект!
print(shoplist,'\n')

del shoplist[0]
print('Удалили первый элемент списка')

print('shoplist:', shoplist)
print('mylist:', mylist)

print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # Создаем копию путем полной вырезки
del mylist[0] # Удаляем первый элемент списка mylist

print('shoplist:', shoplist)
print('mylist:', mylist)