
from datetime import datetime


def decorator(func):
    def wrapper(*args, **kvargs):
        time = datetime.now()
        result = func(*args, **kvargs)
        print("Used time:", datetime.now() - time)
        return result
    return wrapper


@decorator
def first():
    print('Время для печати...')


@decorator
def second():
    lst = []
    for i in range(200):
        import random
        random_number = random.randint(1, 10)
        lst.append(random_number)
    print('Список рандом 200', lst)


import random
random_number = random.randint(1, 10)


first()
second()
