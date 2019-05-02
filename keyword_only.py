# Имя файла keyword_only.py

def total(initial = 5, *numbers, extra_number):
    count = initial
    for every_number in numbers:
        count += every_number # сокращенная запись от: count = count + every_number
    count += extra_number  # сокращенная запись от: count = count + extra_number
    print('Результат: ', count)
# ================================================

total(10, 1, 2, 3, extra_number = 50)
#total(10, 1, 2, 3)
