class Persona:
    def __init__(self, nombre, edad, direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_direccion(self):
        return self.__direccion
    
    def mostrar_info_personal(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, Dirección: {self.__direccion}")
    
    def asignar_rol(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, matricula, carrera):
        super().__init__(nombre, edad, direccion)
        self.__matricula = matricula
        self.__carrera = carrera
    
    def asignar_rol(self):
        return "Estudiante"
    
    def mostrar_info_rol(self):
        print(f"Matrícula: {self.__matricula}, Carrera: {self.__carrera}")

class Profesor(Persona):
    def __init__(self, nombre, edad, direccion, id_empleado, departamento):
        super().__init__(nombre, edad, direccion)
        self.__id_empleado = id_empleado
        self.__departamento = departamento
    
    def asignar_rol(self):
        return "Profesor"
    
    def mostrar_info_rol(self):
        print(f"ID Empleado: {self.__id_empleado}, Departamento: {self.__departamento}")

