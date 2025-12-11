class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.__nombre = nombre
        self.__salario = max(0, salario)
        self.__departamento = departamento

    def aumentar_salario(self, porcentaje):
        if porcentaje > 0:
            self.__salario += self.__salario * porcentaje / 100

    def mostrar_informacion(self):
        return f"{self.__nombre}, {self.__departamento}, ${self.__salario:.2f}"

    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    def get_departamento(self):
        return self.__departamento