class Tienda:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__inventario = []
        self.__ventas_totales = 0
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def mostrar_info_general(self):
        print(f"Tienda: {self.__nombre}, Dirección: {self.__direccion}")
    
    def agregar_producto(self, producto):
        self.__inventario.append(producto)
    
    def eliminar_producto(self, producto):
        if producto in self.__inventario:
            self.__inventario.remove(producto)
    
    def calcular_total_ventas(self):
        pass

class TiendaRopa(Tienda):
    def __init__(self, nombre, direccion, tipo_ropa):
        super().__init__(nombre, direccion)
        self.__tipo_ropa = tipo_ropa
    
    def calcular_total_ventas(self):
        total = 0
        for producto in self._Tienda__inventario:
            total += producto.get_precio()
        self._Tienda__ventas_totales = total
        return total

class TiendaElectronica(Tienda):
    def __init__(self, nombre, direccion, especialidad):
        super().__init__(nombre, direccion)
        self.__especialidad = especialidad
    
    def calcular_total_ventas(self):
        total = 0
        for producto in self._Tienda__inventario:
            total += producto.get_precio()
        self._Tienda__ventas_totales = total
        return total

