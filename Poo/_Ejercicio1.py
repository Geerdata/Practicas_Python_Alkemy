class Vuelo:
    def __init__(self, cantidad_asientos):
        self.capacidad = cantidad_asientos
        self.pasajeros = []

    
    def agregar_pasajeros(self, nombre):
        if  self.cantidad_asientos_disponibles() > 0:
            self.pasajeros.append(nombre)
            return True
        else:
            return False

    def cantidad_asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)


vuelo = Vuelo(7)

personas = ["Karina", "Maria", "Ruben","Carla"]
for persona in personas:
    if vuelo.agregar_pasajeros(persona):
       print(f'La persona {persona} se pudo agregar correctamente al vuelo') 
    else:
        print(f'La persona {persona} No se pudo agregar correctamente al vuelo porque no existen lugares disponibles') 

print(f'Asientos disponibles del vuelo: {vuelo.cantidad_asientos_disponibles()}')