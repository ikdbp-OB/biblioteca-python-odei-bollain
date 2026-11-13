from errores.error import DatosIncorrectos
from almacenamiento import guardar_datos
import biblioteca as ctrl

def menu(libros, socios):
    cerrar = 0
    while (cerrar == 0):
        print("------------BIBLIOTECA------------")
        print("1.Mostrar lista libros")
        print("2.Mostrar libros disponibles")
        print("3.Buscar libro por titulo")
        print("4.Prestar libro")
        print("5.Devolver libro")
        print("6.Mostrar socio con libro")
        print("7.Añadir libro")
        print("8.Salir")
        print("----------------------------------")
        num = int(input("Indica un numero la opción que requieras\n"))
        match num:
            case 1:
                vista_listar_libros(libros)
            case 2:
                vista_listar_disponibles(libros)
            case 3:
                vista_buscar_titulo(libros)
            case 4:
                vista_prestar_libro(libros, socios)
            case 5:
                vista_devolver_libro(libros, socios)
            case 6:
                vista_socios_con_libro(libros, socios)
            case 7:
                vista_anadir_datos(libros, socios)
            case 8:
                res = input("¿Seguro que quieres cerrar el programa? Si o No\n")
                if (res == "Si"):
                    cerrar = 1
                else:
                    print("Volviendo al programa ...")
    print("Cerrando programa...")
def vista_listar_libros(libros):
    print("\n---LISTA DE TODOS LOS LIBROS---")
    if not libros:
        print("No hay libros registrados.")
        return
    for libro in libros:
        print(libro)

def vista_listar_disponibles(libros):
    print("\n---LIBROS DISPONIBLES---")
    disponibles = ctrl.obtener_disponibles(libros)
    if not disponibles:
        print("No hay libros disponibles en este momento.")
        return
    for libro in disponibles:
        print(libro)

def vista_buscar_titulo(libros):
    termino = input("Introduce el término a buscar en el título: ")
    encontrados = ctrl.buscar_por_titulo(libros, termino)
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} coincidencia(s):")
        for libro in encontrados:
            print(libro)
    else:
        print("No existe ningún libro con ese título.")

def vista_prestar_libro(libros, socios):
    cod_libro = input("Código del libro: ").strip()
    cod_socio = input("Código del socio: ").strip()
    try:
        libro, socio = ctrl.realizar_prestamo(libros, socios, cod_libro, cod_socio)
        print(f"Préstamo realizado: '{libro.titulo}' prestado a {socio.nombre}.")
    except DatosIncorrectos as e:
        print(f"Error en préstamo: {e.mensaje} (Dato implicado: {e.dato_erroneo})")

def vista_devolver_libro(libros, socios):
    cod_socio = input("Código del socio que devuelve el libro: ").strip()
    try:
        socio, cod_libro = ctrl.realizar_devolucion(libros, socios, cod_socio)
        print(f"Devolución completada: {socio.nombre} devolvió el libro '{cod_libro}'.")
    except DatosIncorrectos as e:
        print(f"Error en devolución: {e.mensaje} (Dato implicado: {e.dato_erroneo})")

def vista_socios_con_libro(libros, socios):
    print("\n--- SOCIOS CON LIBROS PRESTADOS ---")
    lista = ctrl.obtener_socios_con_libro(libros, socios)
    if not lista:
        print("Ningún socio tiene libros prestados actualmente.")
        return
    for socio, titulo in lista:
        print(f"[{socio.codigoS}] {socio.nombre} -> Tiene: [{socio.cod_libro}] {titulo}")

def vista_anadir_datos(libros, socios):
    opcion = input("¿Qué deseas añadir? (1. Libro / 2. Socio): ").strip()
    try:
        if opcion == "1":
            cod = input("Código del libro: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            año = input("Año: ").strip()
            categoria = input("Categoría: ").strip()
            ctrl.registrar_libro(libros, cod, titulo, autor, año, categoria)
            print("Libro añadido correctamente.")
        elif opcion == "2":
            cod = input("Código del socio: ").strip()
            nombre = input("Nombre: ").strip()
            email = input("Email: ").strip()
            ctrl.registrar_socio(socios, cod, nombre, email)
            print("Socio añadido correctamente.")
        else:
            print("Opción no válida.")
    except DatosIncorrectos as e:
        print(f"Error al añadir: {e.mensaje} (Dato implicado: {e.dato_erroneo})")