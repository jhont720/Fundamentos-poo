class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def emitir_sonido(self):
        pass
    
    def mostrar_detalles(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad} años")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza
    
    def emitir_sonido(self):
        return "Guau guau"
    
    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Raza: {self.__raza}, Sonido: {self.emitir_sonido()}")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.__color = color
    
    def emitir_sonido(self):
        return "Miau miau"
    
    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Color: {self.__color}, Sonido: {self.emitir_sonido()}")
