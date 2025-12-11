
class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.__nombre = nombre
        self.__salario = salario
        self.__cargo = cargo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_salario(self):
        return self.__salario
    
    def get_cargo(self):
        return self.__cargo
    
    def calcular_aumento(self):
        pass

class Gerente(Empleado):
    def __init__(self, nombre, salario, cargo, bono):
        super().__init__(nombre, salario, cargo)
        self.__bono = bono
    
    def calcular_aumento(self):
        return self.get_salario() * 0.20 + self.__bono

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, salario, cargo, meses_contrato):
        super().__init__(nombre, salario, cargo)
        self.__meses_contrato = meses_contrato
    
    def calcular_aumento(self):
        if self.__meses_contrato > 12:
            return self.get_salario() * 0.10
        return self.get_salario() * 0.05

