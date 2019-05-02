# Имя файла user_input.py

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    a = text.replace(' ', '')
    b = a.lower()
    print(b)
    return b == reverse(b)

something = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром - ", something)
else:
    print("Нет, это не палиндром - ", something)

print('Выход.')