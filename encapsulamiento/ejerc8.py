class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = max(0, precio)
        self.__stock = max(0, stock)

    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad

    def disminuir_stock(self, cantidad):
        if 0 < cantidad <= self.__stock:
            self.__stock -= cantidad

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock
