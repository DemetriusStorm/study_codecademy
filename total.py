# Имя файла total.py

def total(initial = 5, *numbers, **keywords):
    count = initial
    for every_number in numbers:
        count += every_number
    for every_key in keywords:
        count +=keywords[every_key]
    return count

print('Итого наименований: ', total(10, 1, 2, vegetables = 50, fruits = 100, beer = 25))