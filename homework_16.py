
odyn = input('Строка 1')
dva = input('Строка 2')
tri = input('Строка 3')
tchotyry = input('Строка 4')

odyn_dva = odyn + '\n' + dva + '\n'
tri_tchotyry = tri + '\n' + tchotyry

file = open('homework_16.txt','w')
file.write(odyn_dva)
file.close()

file = open('homework_16.txt','a')
file.write(tri_tchotyry)
file.close()
