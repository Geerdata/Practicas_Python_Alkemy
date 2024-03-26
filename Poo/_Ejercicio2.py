class Vendedor:
    def __init__(self, nombre, antiguedad, sueldo_basico,categoria, cantidad_autos_vendidos=0):
        self.nombre = nombre
        self.antiguedad = antiguedad
        self.sueldo_basico = sueldo_basico
        self.categoria = categoria
        self.cantidad_autos_vendidos = cantidad_autos_vendidos
    
    def incrementar_autos_vendidos(self, cantidad):
        self.cantidad_autos_vendidos += cantidad

    def calcular_sueldo_total(self):
        pass

    