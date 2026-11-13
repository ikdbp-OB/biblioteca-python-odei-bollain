class DatosIncorrectos(Exception):
    def __init__(self, mensaje, dato_erroneo=None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dato_erroneo = dato_erroneo