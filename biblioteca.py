from modelo.libro import Libro
from modelo.socio import Socio
from errores.error import DatosIncorrectos
from almacenamiento import registrar_log

def obtener_disponibles(libros):
    return [libro for libro in libros if libro.esta_disponible()]