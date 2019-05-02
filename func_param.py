# Имя файла func_param.py

def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')
#=====================================                
printMax(3, 4) # прямая передача параметров

x = 5
y = 7
printMax(x, y) # передача переменных в качестве аргументов