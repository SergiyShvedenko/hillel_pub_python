
values = [1, 2, '3', 'forth', 'end', 99, True, None]

element = list(map(lambda x: str(x) if type(x) is int else x, values))

print(values, element)
