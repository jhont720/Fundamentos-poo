class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion

    def descripcion(self):
        return f"'{self.__titulo}' por {self.__autor}"

    def es_clasico(self):
        from datetime import datetime
        return datetime.now().year - self.__año_publicacion > 50

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_año_publicacion(self):
        return self.__año_publicacion
