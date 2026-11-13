from modelo.libro import Libro
from modelo.socio import Socio
from errores.error import DatosIncorrectos
from almacenamiento import registrar_log

def obtener_disponibles(libros):
    return [libro for libro in libros if libro.esta_disponible()]

def buscar_por_titulo(libros, termino):
    termino_limpio = termino.strip().lower()
    if not termino_limpio:
        return []
    return [libro for libro in libros if termino_limpio in libro.titulo.lower()]

def realizar_prestamo(libros, socios, cod_libro, cod_socio):
    libro = next((l for l in libros if l.codigoL == cod_libro), None)
    socio = next((s for s in socios if s.codigoS == cod_socio), None)

    if not libro:
        raise DatosIncorrectos("El código de libro no existe", cod_libro)
    if not socio:
        raise DatosIncorrectos("El código de socio no existe", cod_socio)
    if not libro.esta_disponible():
        raise DatosIncorrectos(f"El libro ya está prestado al socio {libro.cod_socio}", libro.codigoL)
    if socio.tiene_libro():
        raise DatosIncorrectos(f"El socio ya tiene prestado el libro {socio.cod_libro}", socio.codigoS)

    libro.prestar(cod_socio)
    socio.tomar_libro(cod_libro)
    registrar_log("PRESTAMO", f"Libro {cod_libro} prestado al socio {cod_socio}")
    return libro, socio

def realizar_devolucion(libros, socios, cod_socio):
    socio = next((s for s in socios if s.codigoS == cod_socio), None)
    if not socio:
        raise DatosIncorrectos("El código de socio no existe", cod_socio)

    cod_libro = socio.devolver_libro()
    libro = next((l for l in libros if l.codigoL == cod_libro), None)
    if libro:
        libro.devolver()

    registrar_log("DEVOLUCION", f"Socio {cod_socio} devolvió el libro {cod_libro}")
    return socio, cod_libro