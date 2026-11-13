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

def guardar_datos(libros, socios, ruta_libros="datos/libros.txt", ruta_socios="datos/socios.txt"):
    with open(ruta_libros, "w", encoding="utf-8") as f:
        for l in libros:
            socio_txt = l.cod_socio if l.cod_socio is not None else "none"
            f.write(f"{l.codigoL},{l.titulo},{l.autor},{l.año},{l.categoria},{socio_txt}\n")

    with open(ruta_socios, "w", encoding="utf-8") as f:
        for s in socios:
            libro_txt = s.cod_libro if s.cod_libro is not None else "none"
            f.write(f"{s.codigoS},{s.nombre},{s.email},{libro_txt}\n")