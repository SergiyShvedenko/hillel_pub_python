
import random
random_number = random.randint(1, 10)
for i in range(5):

    while True:
        input_number = input('С пяти раз угадайте число от 0 до 10: ')
        if input_number.isdigit() and int(input_number) >= 0 and int(input_number) <= 21:
            break
        print('Bam нужно внимательно вводить число от 0 до 21')

    if random_number == int(input_number):
        print("Вітаємо, Вам в артилеристи! Ваші дані передані воєнкому, очікуйте повістку...  ")
        break
else:
    print('Жаль, попробуйте снова!')

print('Верное число: ', random_number)
