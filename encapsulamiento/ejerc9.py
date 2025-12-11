class Juego:
    def __init__(self, nombre, genero, precio):
        self.__nombre = nombre
        self.__genero = genero
        self.__precio = max(0, precio)

    def mostrar_informacion(self):
        return f"{self.__nombre} ({self.__genero}) - ${self.__precio:.2f}"

    def esta_en_oferta(self, limite):
        return self.__precio < limite

    def get_nombre(self):
        return self.__nombre

    def get_genero(self):
        return self.__genero

    def get_precio(self):
        return self.__precio
