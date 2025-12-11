class Transporte:
    def __init__(self, capacidad, velocidad_maxima):
        self.__capacidad = capacidad
        self.__velocidad_maxima = velocidad_maxima
    
    def get_capacidad(self):
        return self.__capacidad
    
    def get_velocidad_maxima(self):
        return self.__velocidad_maxima
    
    def tiempo_viaje(self, distancia):
        pass

class Avion(Transporte):
    def __init__(self, capacidad, velocidad_maxima, tipo_motor):
        super().__init__(capacidad, velocidad_maxima)
        self.__tipo_motor = tipo_motor
    
    def tiempo_viaje(self, distancia):
        return distancia / self.get_velocidad_maxima()

class Barco(Transporte):
    def __init__(self, capacidad, velocidad_maxima, tipo_casco):
        super().__init__(capacidad, velocidad_maxima)
        self.__tipo_casco = tipo_casco
    
    def tiempo_viaje(self, distancia):
        return distancia / self.get_velocidad_maxima()
