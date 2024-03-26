def cuadrado(x):
    return x + x

print(cuadrado(2))


for i in range(10):
    print(f'El Cuadrado de {i} es {cuadrado(i)}')


#Calcular Edad
def calcular_edad(anio_nacimiento, anio_actual):
    edad = anio_actual - anio_nacimiento
    return edad

print(f'Edad : {calcular_edad(1956,2024)}')


#Sumar Numeros
#Recibe dato como tupla
def sumar_numeros(*numeros):
    print(f'Tipo de variable numeros : {type(numeros)}')
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar_numeros(2,3,5,9,4,6))

#Recibe dato como diccionario
def mostrar_datos(**data):
    print(f'tipo de datos de data : {type(data)}')
    for nombre, valor in data.items():
        print(f'{nombre}: {valor}')
        
mostrar_datos(nombre='Luisa', edad=34, oficio= 'Instructora')
