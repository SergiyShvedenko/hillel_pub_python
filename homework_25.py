import math


class NegativNumberException(Exception):
    pass


class Main(object):

    def __init__(self):
        self.x = x
        self.y = y

    @classmethod
    def add(cls, x, y):
        try:
            result = int(x) + int(y)
        except ValueError:
            print('Не введено число')
        else:
            print('Результат:', result)

    @classmethod
    def sub(cls, x, y):
        try:
            result = int(x) - int(y)
        except ValueError:
            print('Не введено число')
        else:
            print('Результат:', result)

    @classmethod
    def div(cls, x, y):
        try:
            result = int(x) / int(y)
        except ValueError:
            print('Не введено число, повторите ввод...')
        except ZeroDivisionError:
            print('На ноль делить нельзя, повторите ввод...')
        else:
            print('Результат:', result)

    @classmethod
    def mul(cls, x, y):
        try:
            result = int(x) * int(y)
        except ValueError:
            print('Не введено число, повторите ввод...')
        else:
            print('Результат:', result)

    @classmethod
    def pow(cls, x, y):
        try:
            result = int(x) ** int(y)
        except ValueError:
            print('Не введено число, повторите ввод...')
        else:
            print('Результат:', result)

    @classmethod
    def sqrt(cls, x,):
        try:
            if int(x) < 0:
                raise NegativNumberException
        except NegativNumberException:
            print('Введено отрицательное число, повторите ввод...')
        except ValueError:
            print('Не введено число, повторите ввод...')
        else:
            result = math.sqrt(int(x))
            print('Результат:', result)


while True:
    z = input('Действия: \n \t 0 - стоп  \t \t 1 - сложение \t 2 - вычитание \
     \t 3 - деление\n \t 4 - умножение \t 5 - возведение\
     в степень \t 6 - извлечение квадратного корня \n ')
    if z == '0':
        break
    if z == '6':
        x = input('Число: ')
        result = Main()
        result.sqrt(x)
    else:
        x = input('Первое число: ')
        y = input('Второе число: ')
        if z == '1':
            result = Main()
            result.add(x, y)
        if z == '2':
            result = Main()
            result.sub(x, y)
        if z == '3':
            result = Main()
            result.div(x, y)
        if z == '4':
            result = Main()
            result.mul(x, y)
        if z == '5':
            result = Main()
            result.pow(x, y)

