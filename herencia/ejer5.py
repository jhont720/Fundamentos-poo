import datetime

class Producto:
    def __init__(self, nombre, precio, fecha_vencimiento):
        self.__nombre = nombre
        self.__precio = precio
        self.__fecha_vencimiento = fecha_vencimiento
    
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    
    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento
    
    def aplicar_descuento(self):
        pass

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, fecha_vencimiento, perecedero):
        super().__init__(nombre, precio, fecha_vencimiento)
        self.__perecedero = perecedero
    
    def aplicar_descuento(self):
        hoy = datetime.date.today()
        if self.__perecedero and (self.get_fecha_vencimiento() - hoy).days <= 7:
            return self.get_precio() * 0.70
        return self.get_precio()

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, fecha_vencimiento, garantia_meses):
        super().__init__(nombre, precio, fecha_vencimiento)
        self.__garantia_meses = garantia_meses
    
    def aplicar_descuento(self):
        hoy = datetime.date.today()
        if (self.get_fecha_vencimiento() - hoy).days > 365:
            return self.get_precio() * 0.85
        return self.get_precio()
