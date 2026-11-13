from datetime import datetime
from modelo.libro import Libro
from modelo.socio import Socio

def cargar_libros(ruta="datos/libros.txt"):
    libros = []
    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            codigoL, titulo, autor, año, categoria, cod_socio = line.strip().split(",", 5)
            libros.append(Libro(
                codigoL.strip(),
                titulo.strip(),
                autor.strip(),
                año.strip(),
                categoria.strip(),
                cod_socio.strip()
            ))
    return libros

def cargar_socios(ruta="datos/socios.txt"):
    socios = []
    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            codigoS, nombre, email, cod_libro = line.strip().split(",", 3)
            socios.append(Socio(
                codigoS.strip(),
                nombre.strip(),
                email.strip(),
                cod_libro.strip()
            ))
    return socios