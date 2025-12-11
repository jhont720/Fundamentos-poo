class Figura:
    def __init__(self, nombre, color):
        self.__nombre = nombre
        self.__color = color
    
    def get_nombre(self):
        return self.__nombre
    
    def get_color(self):
        return self.__color
    
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def imprimir_detalles(self):
        print(f"Figura: {self.__nombre}, Color: {self.__color}")

class Circulo(Figura):
    def __init__(self, nombre, color, radio):
        super().__init__(nombre, color)
        self.__radio = radio
    
    def area(self):
        import math
        return math.pi * (self.__radio ** 2)
    
    def perimetro(self):
        import math
        return 2 * math.pi * self.__radio
    
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Radio: {self.__radio}, Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}")

class Rectangulo(Figura):
    def __init__(self, nombre, color, base, altura):
        super().__init__(nombre, color)
        self.__base = base
        self.__altura = altura
    
    def area(self):
        return self.__base * self.__altura
    
    def perimetro(self):
        return 2 * (self.__base + self.__altura)
    
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Base: {self.__base}, Altura: {self.__altura}, Área: {self.area()}, Perímetro: {self.perimetro()}")

