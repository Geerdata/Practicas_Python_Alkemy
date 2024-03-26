nombres = ['Julio', 'Micaela', 'Santi', 'Guido']

#ver cantidad de nombres
print(len(nombres))

#Ver primer nombre
print(nombres[0])

#ver ultimo nombre
print(nombres[-1])

#Otra forma de ver el ultimo nombre
print(nombres[len(nombres)-1])

#Cambia un elemento de la lista
nombres[0] = 'Luis'
print(nombres)

#Agrega un elemento de la lista
nombres.append('Santi')

print(nombres)

#Elimina el ultimo registro de la lista
nombres.pop()
#Elimina el primer registro de la lista
nombres.pop(0)

#Elimina un elemento puntual de la lista
nombres.remove('Santi')

#Inserta un elemento a la lista
nombres.insert(5,'Micaela')


#Agrega un elemento de la lista
nombres.append('Santi')

#Agrega varios elementos a la lista
nombres.extend(['Facu', 'Ramiro'])
print(nombres)