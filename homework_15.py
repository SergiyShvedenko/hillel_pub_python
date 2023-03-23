
code = b'r\xc3\xa9sum\xc3\xa9'

dec = code.decode()
print('Декодировка по умолчанию: ', '\n', '\t', dec)

enc = dec.encode('latin1')
print('Кодировка latin1: ', '\n', '\t', enc)

dec = enc.decode('latin1')
print('Декодировка latin1: ', '\n', '\t', dec)
