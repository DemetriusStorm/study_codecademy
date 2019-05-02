# Имф файла class_init.py

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет! Меня зовут', self.name)
        
p = Person('Demetrius')
p.sayHi()
