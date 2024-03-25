#Variables primitivas
a = 28
b = 1.5
c = 'Hola'
d = True
e = None
rango_10 = range(10)

#print(rango_10)
#print(type(d))

#Desempáquetado de variables 
#ACLARACION : Si surgen el siguiente conflicto "ValueError: too many values to unpack (expected 5)" en este caso python necesita que el indique el limite de la variable con (*) asterisco en la ultima variable

y, i, k, l, *m = "python"

print(a)
print(i)
print(k)
print(l)
print(m)

print(f'Suma a+b :  {a+b}')

print(type(a))

#operador de control
print(f'Es la variable a menor a 30? {a<30}')

#operador logico de comparación (AND)
print(3 > 2 and 4 < 7)   # Si se utiliza and debe ser verdadero ambas condiciones deben ser verdaderas

#operador logico de comparación (OR) 
print(3 > 2 and 4 < 7)   # Si se utiliza and debe ser verdadero solo una condicion sea verdadera


#operaciones de negación
print(f'La variable e es None? {e is not None}')


cadena = 'German'
texto_concatenado = cadena + " es Especialista en Data Science"
print(texto_concatenado)

nombre = "German Rodriguez"

nombre_mayuscula = nombre.upper()
nombre_minuscula = nombre.lower()

print(nombre_mayuscula)
print(nombre_minuscula)