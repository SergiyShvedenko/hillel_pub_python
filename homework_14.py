

def enter():
    while True:
        input_value = input(
            'Введите число или одно из значений: "выход", "exit", "quit", "e" или "q" в любом регистре: ')
        if input_value.lower() == 'выход' or input_value.lower() == 'exit' \
                or input_value.lower() == 'quit' or input_value.lower() == 'e' \
                or input_value.lower() == 'q':
            break
        while True:

            list1 = list(input_value)
            i = ','
            if i in list1:
                new_n_name = '.'
                list1 = [a if a != i else new_n_name for a in list1]
                if list1.count('.') > 1:
                    print('Вы ввели не корректное число:', input_value)
                    break
                db = ''.join(list1)
                check_txt = db.replace('-', '')
                check_txt = check_txt.replace('.', '')
                if not check_txt.isdigit():
                    print('Вы ввели не корректное число:', input_value)
                    break
                db = float(db)
                if db == 0:
                    print('Вы ввели ноль')
                    break
                if db < 0:
                    print('Вы ввели отрицательное дробное число:', input_value)
                    break
                if db > 0:
                    print('Вы ввели положительное дробное число:', input_value)
                    break
            i = '.'
            if i in list1:
                new_n_name = '.'
                list1 = [a if a != i else new_n_name for a in list1]
                if list1.count('.') > 1:
                    print('Вы ввели не корректное число:', input_value)
                    break
                db = ''.join(list1)
                check_txt = db.replace('-', '')
                check_txt = check_txt.replace('.', '')
                if not check_txt.isdigit():
                    print('Вы ввели не корректное число:', input_value)
                    break
                db = float(db)
                if db == 0:
                    print('Вы ввели ноль')
                    break
                if db < 0:
                    print('Вы ввели отрицательное дробное число:', input_value)
                    break
                if db > 0:
                    print('Вы ввели положительное дробное число:', input_value)
                    break
            if input_value.isdigit():
                if int(input_value) == 0:
                    print('Вы ввели ноль')
                    break
                if int(input_value) > 0:
                    print('Вы ввели положительное целое число:', input_value)
                    break
            if input_value[0] == '-' and input_value[1:].isdigit():
                print('Вы ввели отрицательное целое число:', input_value)
                break
            print('Вы ввели не корректное число:', input_value)
            break


enter()
