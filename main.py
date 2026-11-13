from almacenamiento import cargar_libros, cargar_socios
from menu import menu

def main():
    try:
        libros = cargar_libros("datos/libros.txt")
        socios = cargar_socios("datos/socios.txt")
        print(f"Se ha cargado correctamente la información de {len(libros)} libros y {len(socios)} socios.")
        
        menu(libros, socios)
    except FileNotFoundError as e:
        print(f"Error crítico: No se encontró el archivo de datos ({e.filename}).")

if __name__ == "__main__":
    main()