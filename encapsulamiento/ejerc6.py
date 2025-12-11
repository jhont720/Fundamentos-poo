class Rectangulo:
    def __init__(self, base, altura):
        self.__base = max(0, base)
        self.__altura = max(0, altura)

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2 * (self.__base + self.__altura)

    def get_base(self):
        return self.__base

    def set_base(self, base):
        if base >= 0:
            self.__base = base

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        if altura >= 0:
            self.__altura = altura