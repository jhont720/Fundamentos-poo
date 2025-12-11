import math

class Circulo:
    def __init__(self, radio):
        self.__radio = max(0, radio)

    def area(self):
        return math.pi * self.__radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.__radio

    def get_radio(self):
        return self.__radio

    def set_radio(self, radio):
        if radio >= 0:
            self.__radio = radio