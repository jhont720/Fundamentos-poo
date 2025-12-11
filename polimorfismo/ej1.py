class Figura:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.__radio = radio
    
    def area(self):
        import math
        return math.pi * (self.__radio ** 2)
    
    def get_radio(self):
        return self.__radio

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.__base = base
        self.__altura = altura
    
    def area(self):
        return self.__base * self.__altura
    
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
figuras = [
    Circulo("Círculo 1", 5),
    Rectangulo("Rectángulo 1", 4, 6),
    Circulo("Círculo 2", 3)
]

for figura in figuras:
    print(f"{figura.get_nombre()}: Área = {figura.area():.2f}")