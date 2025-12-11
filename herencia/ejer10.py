class Pago:
    def __init__(self, monto, fecha):
        self.__monto = monto
        self.__fecha = fecha
    
    def get_monto(self):
        return self.__monto
    
    def get_fecha(self):
        return self.__fecha
    
    def procesar_pago(self):
        pass
    
    def generar_recibo(self):
        pass
    
    def mostrar_detalles(self):
        print(f"Pago de ${self.__monto} realizado el {self.__fecha}")

class PagoTarjeta(Pago):
    def __init__(self, monto, fecha, numero_tarjeta, cvv):
        super().__init__(monto, fecha)
        self.__numero_tarjeta = numero_tarjeta
        self.__cvv = cvv
    
    def procesar_pago(self):
        return f"Procesando pago con tarjeta terminada en {self.__numero_tarjeta[-4:]}"
    
    def generar_recibo(self):
        return f"Recibo por ${self.get_monto()} - Tarjeta: {self.__numero_tarjeta}"

class PagoPayPal(Pago):
    def __init__(self, monto, fecha, email):
        super().__init__(monto, fecha)
        self.__email = email
    
    def procesar_pago(self):
        return f"Procesando pago con PayPal desde {self.__email}"
    
    def generar_recibo(self):
        return f"Recibo por ${self.get_monto()} - PayPal: {self.__email}"