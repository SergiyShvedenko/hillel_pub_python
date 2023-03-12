
# Формирование списка:
lst = []
for i in range(200):
    import random
    random_number = random.randint(1, 10)
    lst.append(random_number)
print('Список рандом 200', lst)


# Функция сортировки списка:
def sort():
    for el in lst:
        if rez.get(el, None):
            rez[el] += 1
        else:
            rez[el] = 1

            
rez = {}
sort()
print('Словарь - результат', rez)

rez_sorted = sorted(rez.items())
print(dict(rez_sorted))
