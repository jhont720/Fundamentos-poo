class Coche:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def mostrar_informacion(self):
        return f"{self.__marca} {self.__modelo} ({self.__año})"

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        if marca.strip():
            self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        if modelo.strip():
            self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        if 1886 <= año <= 2025:
            self.__año = año
