from errores.error import DatosIncorrectos

class Libro:
    def __init__(self, codigoL, titulo, autor, año, categoria, cod_socio):
        self.codigoL = codigoL
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.categoria = categoria
        self.cod_socio = cod_socio

    def esta_disponible(self):
        return self.cod_socio is None

    def prestar(self, cod_socio):
        if not self.esta_disponible():
            raise DatosIncorrectos(f"El libro ya está prestado al socio {self.cod_socio}", self.codigoL)
        self.cod_socio = cod_socio

    def devolver(self):
        self.cod_socio = None
    
    def __str__(self):
        return f'Codigo del Libro: {self.codigoL}, Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Categoria: {self.categoria}'