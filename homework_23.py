
class String():

    def __init__(self, x=0):
        self.x = str(x)

    def __add__(self, other):
        x = self.x + other.x
        return String(x)

    def __str__(self):
        return f'({self.x})'

    def __sub__(self, other):
        x = self.x
        y = other.x
        return String(x.replace(y, '', 1))
