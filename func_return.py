# Имя файла func_return.py

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y
# ======================================    
print('Что больше, 2 или 3?', maximum(2, 3))
print('Что больше, 2 или 2?', maximum(2, 2))
print('Что больше, 10 или 5?', maximum(10, 5))

# Существует встроенная функция max,
# в которой уже реализован функционал поиск максимума
# ======================================   
print()
def someFunction ():
    pass
print(someFunction())