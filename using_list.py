# Имя файла using_list.py

# Этой мой список покупок
shoplist = ['яблоки', 'молоко', 'хлеб', 'мука', 'соль']

print('Я должен сделать', len(shoplist), 'покупок')

print('А именно:', end = ' ')
for item in shoplist:
    print(item, end = ' ')
    
print('\n\nТак же нужно купить риса, добавим его в список!')
shoplist.append('рис')
print('Вот новый список покупок:', shoplist)

print('\nСделаем сортировку списка!')
shoplist.sort()
print('Вот отсортированный список покупок:', shoplist)

print('\nПервое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Только что купил', olditem)
print('Вот что осталось купить:', shoplist)
