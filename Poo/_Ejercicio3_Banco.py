from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, saldo):
        self.saldo = saldo

    @abstractmethod
    def extraer(self, monto):
        pass

    def depositar(self,monto):
        self.saldo += monto    
    
    def consultar_saldo(self):
        return f'Saldo Actual {self.saldo}'


class CajaAhorro(CuentaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)

    def extraer(self, monto):
        if monto > self.saldo:
           return f'Fondos insuficientes'
        else:
            self.saldo -= monto
            return f'Se realizo al extraccion - Saldo Actual: {self.saldo}' 


class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo, Limite_descubierto=100000):
        super().__init__(saldo)
        self.limite_descubierto = Limite_descubierto

    def extraer(self, monto):
        if monto > self.saldo + self.limite_descubierto:
           return f'Fondos insuficientes, se supero el limite al descubierto'
        else:
            self.saldo -= monto
            return f'Se realizo al extraccion - Saldo Actual: {self.saldo}' 

    def consultar_saldo(self):
        saldo =  super().consultar_saldo()
        return f'{saldo} - Limite al descubierto: {self.limite_descubierto} '

caja_Ahorro = CajaAhorro(200)
caja_Ahorro.depositar(500)
caja_Ahorro.extraer(300)

print(f'Saldo Caja Ahorro : {caja_Ahorro.consultar_saldo()}')



cta_corriente = CuentaCorriente(1000)
cta_corriente.depositar(1000)
print(cta_corriente.extraer(5000))
print(f'Saldo Caja Ahorro : {cta_corriente.consultar_saldo()}')


