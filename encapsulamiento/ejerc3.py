class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.__titular = titular
        self.__saldo = max(0, saldo)
        self.__numero_cuenta = numero_cuenta

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_numero_cuenta(self):
        return self.__numero_cuenta