# Имя файла pickling.py

import pickle

# имя файла, в котором мы сохраним объект
shoplistfile = 'D:\\Temp\\shoplist.data'
# список покупок
shoplist = ['яблоки', 'майонез', 'сахар']

# запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем объект в файл
f.close

del shoplist # уничтожаем переменную shoplist

# считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)

