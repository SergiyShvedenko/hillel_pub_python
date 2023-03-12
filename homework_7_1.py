
def control():
    while True:
        input_value = input('С пяти раз угадайте число от 0 до 10: ')
        if input_value.isdigit() and int(input_value) >= 0 and int(input_value) <= 21:
            break
        print('Bam нужно внимательно вводить число от 0 до 21')
    return input_value

import random
random_number = random.randint(1, 10)

for i in range(5):

    valid = control()
    if int(valid) == random_number:
        print("Вітаємо, Вам в артилеристи!...  ")
        break
else:
    print('Жаль, попробуйте снова!')

print('Верное число: ', random_number)
