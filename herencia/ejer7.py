class Instrumento:
    def __init__(self, nombre, material):
        self.__nombre = nombre
        self.__material = material
    
    def get_nombre(self):
        return self.__nombre
    
    def get_material(self):
        return self.__material
    
    def tipo_sonido(self):
        pass
    
    def tocar_nota(self, nota):
        pass

class Guitarra(Instrumento):
    def __init__(self, nombre, material, cuerdas):
        super().__init__(nombre, material)
        self.__cuerdas = cuerdas
    
    def tipo_sonido(self):
        return "Melódico"
    
    def tocar_nota(self, nota):
        return f"Tocando nota {nota} en la guitarra"

class Piano(Instrumento):
    def __init__(self, nombre, material, teclas):
        super().__init__(nombre, material)
        self.__teclas = teclas
    
    def tipo_sonido(self):
        return "Armónico"
    
    def tocar_nota(self, nota):
        return f"Presionando tecla {nota} en el piano"

