frutas = ('banana', 'manzana', 'pera', 'limon')
print(frutas[2])

print(frutas[1:])

print(frutas[0:3])


lista = list(frutas)
print(lista)

tupla = tuple(lista)
print(tupla)

total = frutas + ('kiwi',)
print(total)

tupla2 = ('a', 'b',[1,2])
print(tupla2)

tupla2[2].append(3)
print(tupla2)
