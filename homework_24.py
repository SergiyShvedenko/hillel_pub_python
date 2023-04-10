
class Sklad():

    FREE_PLACES = 10

    def __init__(self, model, year=2023):
        self.model = model
        self.year = year
        Sklad.FREE_PLACES -= 1

    @classmethod
    def total_objects(cls):
        print('Free places:', cls.FREE_PLACES)

    @staticmethod
    def check_total():
        if Sklad.FREE_PLACES > 0:
            print('Free!')
        else:
            print('FULL!')

    @staticmethod
    def balance():
        if Tires.TOTAL_TIRES == Wheels.TOTAL_WHEELS:
            print('Good job!!!')
        else:
            print('Need control!')


class Tires(Sklad):

    TOTAL_TIRES = 0

    def __init__(self, model, year):
        super().__init__(Sklad)
        Tires.TOTAL_TIRES += 1

    @classmethod
    def total_tires(cls):
        print('Tires:', cls.TOTAL_TIRES)


class Wheels(Sklad):

    TOTAL_WHEELS = 0

    def __init__(self, model, year):
        super().__init__(Sklad)
        Wheels.TOTAL_WHEELS += 1


    @classmethod
    def total_wheels(cls):
        print('Wheels:', cls.TOTAL_WHEELS)


tires_1 = Tires('pirelli', 2020)
wheel_1 = Wheels('Porche', 2021)
wheel_2 = Wheels('Porche', 2021)
wheel_3 = Wheels('BORBET', 2022)
tires_2 = Tires('Toyo', 2021)
tires_2 = Tires('Toyo', 2021)
Sklad.total_objects()
Wheels.total_wheels()
Tires.total_tires()
Sklad.check_total()
Sklad.balance()