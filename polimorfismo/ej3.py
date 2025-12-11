class Vehiculo:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def mover(self):
        pass

class Coche(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def mover(self):
        return "El coche se mueve en 4 ruedas"

class Bicicleta(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def mover(self):
        return "La bicicleta se mueve pedaleando"

# Ejemplo de uso polimórfico
def mover_vehiculos(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print(f"{vehiculo.get_nombre()}: {vehiculo.mover()}")

vehiculos = [
    Coche("Toyota Corolla"),
    Bicicleta("BMX"),
    Coche("Ford Mustang"),
    Bicicleta("Montaña")
]

mover_vehiculos(vehiculos)
