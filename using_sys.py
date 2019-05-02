# Имя файла using_sys.py

import sys

print ('Аргументы командной строки: ')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

# =========================================================
import os; print('Текущий каталог программы:', os.getcwd())

