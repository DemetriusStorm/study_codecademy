# Имя файла using_tuple.py

old_zoo = ('питон', 'слон', 'пингвин') # Скобки не обязательны
print('Всего животных в зоопарке -', len(old_zoo))

new_zoo = 'обезьяна', 'верблюд', old_zoo
print('Всего КЛЕТОК в зоопарке -', len(new_zoo))

print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезенные из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезенное из старого зоопарка -', new_zoo[2][2])
print('Всего животных в новом зоопарке -', len(new_zoo)-1+len(new_zoo[2]))