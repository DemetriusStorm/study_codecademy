# Имя файла raising.py

class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, length,  atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        
try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputExceprion: Длина введенной строки -- {};\
 ожидалось, как минимум, {}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений.')