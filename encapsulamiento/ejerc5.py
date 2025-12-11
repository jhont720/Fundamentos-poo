class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 20:
            self.__notas.append(nota)

    def calcular_promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_notas(self):
        return self.__notas.copy()