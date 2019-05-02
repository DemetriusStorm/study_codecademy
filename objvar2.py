# Имя файла objvar.py

class Robot:
    """Представляет робота с именем."""
    # Переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        """Инициализация данных."""
        self.name = name
        print("(Инициализация {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """Я умираю."""
        print("{} уничтожается!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} был последним.".format(self.name))
        else:
            print("Осталось {:d} работающих роботов.".format(Robot.population))

    def say_hi(self):
        """Приветствие робота.
        
        Да, они это могут."""
        print("Приветствую! Мои хозяева называют меня {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Выводит численность роботов."""
        print("У нас {0:d} роботов.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
droid1.die()
droid2.die()

Robot.how_many()