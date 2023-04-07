
class String(object):

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        x = str(self.x) + str(other)
        return String(x)

    def __sub__(self, other):
        x = str(self.x)
        y = str(other)
        return String(x.replace(y, '', 1))
