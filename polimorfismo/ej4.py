class Empleado:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def calcular_salario(self):
        pass

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas_trabajadas, precio_hora):
        super().__init__(nombre)
        self.__horas_trabajadas = horas_trabajadas
        self.__precio_hora = precio_hora
    
    def calcular_salario(self):
        return self.__horas_trabajadas * self.__precio_hora

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.__salario_mensual = salario_mensual
    
    def calcular_salario(self):
        return self.__salario_mensual

# Ejemplo de uso polimórfico
empleados = [
    EmpleadoPorHora("Juan", 40, 15),
    EmpleadoFijo("María", 2000),
    EmpleadoPorHora("Carlos", 30, 12),
    EmpleadoFijo("Ana", 1800)
]

total_salarios = 0
for empleado in empleados:
    salario = empleado.calcular_salario()
    total_salarios += salario
    print(f"{empleado.get_nombre()}: Salario = ${salario:.2f}")

print(f"Total de salarios a pagar: ${total_salarios:.2f}")
