from errores.error import DatosIncorrectos

class Socio:
    def __init__(self, codigoS, nombre, email, cod_libro=None):
        if "@" not in email:
            raise DatosIncorrectos("El formato del email no es válido", email)
        self.codigoS = codigoS
        self.nombre = nombre
        self.email = email
        self.cod_libro = None if cod_libro in (None, "none", "None", "") else cod_libro

    def tiene_libro(self):
        return self.cod_libro is not None

    def tomar_libro(self, cod_libro):
        if self.tiene_libro():
            raise DatosIncorrectos(f"El socio ya tiene prestado el libro {self.cod_libro}", self.codigoS)
        self.cod_libro = cod_libro

    def devolver_libro(self):
        if not self.tiene_libro():
            raise DatosIncorrectos("Este socio no tiene ningún libro para devolver", self.codigoS)
        libro_devuelto = self.cod_libro
        self.cod_libro = None
        return libro_devuelto

    def __str__(self):
        return f'Codigo de socio: {self.codigoS} Nombre: {self.nombre}, Email: {self.email}'