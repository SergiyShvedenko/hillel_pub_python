

def progression(number, size):
    count = 1
    number1 = number
    while count <= size:
        yield number
        number *= number1
        count += 1


elem = input('Введите число геометрической прогрессии: ')
qual = input('Введите количество членов геометрической прогрессии: ')
prog = progression(int(elem), int(qual))

for item in prog:
    print(item)
