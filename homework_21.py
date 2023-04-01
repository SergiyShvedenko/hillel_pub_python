import time


class Auto(object):
    def __init__(self, brand, age, mark, cоlor='red', weight=1000):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.cоlor = cоlor
        self.weight = weight

    def move(self):
        print('Move!')

    def birthday(self):
        self.age+=1

    def stop(self):
        print('Stop!')


class Truck(Auto):
    def __init__(self, brand, age, mark, cоlor, weight, max_load):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_load = max_load

    def move(self):
        print('Attention!')
        super().move()

    def load(self):
        time.sleep(1)
        print('load!')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, cоlor, weight, max_speed):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_speed = max_speed

    def move(self):
        print('Move!')
        print('max speed is: ', self.max_speed)



truck_1 = Truck('Volvo', 3, 'XF', 'White', None, 25)
print('truck_1', truck_1.brand)
truck_1.load()
truck_1.move()
truck_1.age = 2
truck_1.birthday()
print(truck_1.age)

truck_2 = Truck('Scania', 10, 'XF', 'White', 20, 90)
print('truck_2', truck_2.brand)
truck_2.load()
truck_2.move()

car_1 = Car('Audi', 1, 'A4', 'Red', 1000, 250)
print('car_1', car_1.brand, car_1.age, car_1.mark, car_1.cоlor, car_1.weight, car_1.max_speed)
car_1.move()

car_2 = Car('Mersedes', 4, 'S500', 'Black', 1000, 250)
print('car_2', car_2.brand, car_2.age, car_2.mark, car_2.cоlor, car_2.weight, car_2.max_speed)
car_2.move()