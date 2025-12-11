class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_año(self):
        return self.__año
    
    def eficiencia_combustible(self):
        pass
    
    def combustible_viaje(self, distancia):
        pass

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, consumo):
        super().__init__(marca, modelo, año)
        self.__consumo = consumo
    
    def eficiencia_combustible(self):
        return 100 / self.__consumo
    
    def combustible_viaje(self, distancia):
        return (self.__consumo / 100) * distancia

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, consumo):
        super().__init__(marca, modelo, año)
        self.__consumo = consumo
    
    def eficiencia_combustible(self):
        return 100 / self.__consumo
    
    def combustible_viaje(self, distancia):
        return (self.__consumo / 100) * distancia

