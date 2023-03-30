class Auto:

    def __init__(self, brand, age, mark, cоlor='red', weight=1000):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.cоlor = cоlor
        self.weight = weight

    def move(self):
        print('Move!')

    def birthday(self, age):
        age += 1
        print('birthday', age)

    def stop(self):
        print('Stop!')


auto_1 = Auto('Audi', 2, 'A4')
print(auto_1.brand)
auto_1.birthday(2)
