
inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

output = list(filter(lambda x: x if x[::-1].lower() == x.lower() else False, inputdata))

print(output)
