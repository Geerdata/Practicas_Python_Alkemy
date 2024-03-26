def verificar_tipo(lista):
    tipo_dato = type(lista[0])

    for item in lista:
        if not isinstance(item, tipo_dato):
            return False            

lista1 = [1,2,3]
print(f'Lista1 tiene todos los elementos del mismo tipo: {verificar_tipo(lista1)}')

lista2 = ['f', 'r', 1, True]
print(f'Lista2 tiene todos los elementos del mismo tipo: {verificar_tipo(lista2)}')