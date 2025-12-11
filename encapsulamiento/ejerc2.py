class Persona:
    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo

    def cambiar_edad(self, nueva_edad):
        if 0 <= nueva_edad <= 120:
            self.__edad = nueva_edad

    def mostrar_informacion(self):
        return f"{self.__nombre}, {self.__edad} años, {self.__sexo}"

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo
