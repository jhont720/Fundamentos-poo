class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hacer_sonido(self):
        return "Miau"
animales = [
    Perro("Firulais"),
    Gato("Michi"),
    Perro("Rex"),
    Gato("Luna")
]

for animal in animales:
    print(f"{animal.get_nombre()} dice: {animal.hacer_sonido()}")
