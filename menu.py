from errores.error import DatosIncorrectos
from almacenamiento import guardar_datos
import biblioteca as ctrl

def menu():
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
                libros = listar_libro_disponible()
                print (libros)
            case 3:
                print(3)

            case 4:
                print(4)

            case 5:
                print(5)

            case 6:
                print(6)

            case 7:
                print(7)

            case 8:
                res = input("¿Seguro que quieres cerrar el programa? Si o No\n")
                if (res == "Si"):
                    cerrar = 1
                else:
                    print("Volviendo al programa ...")
    print("Cerrando programa...")
def vista_listar_libros(libros):
    print("\n--- LISTA DE TODOS LOS LIBROS ---")
    if not libros:
        print("No hay libros registrados.")
        return
    for libro in libros:
        print(libro)