# Sistema de Gestión de Biblioteca

Sistema de gestión de biblioteca desarrollado en Python aplicando **Programación Orientada a Objetos (POO)**, programación modular por funciones, manejo de excepciones personalizadas y persistencia de datos en ficheros de texto.

---

## Arquitectura y Estructura del Proyecto

El proyecto está organizado siguiendo el patrón **Modelo-Vista-Controlador (MVC)** para separar responsabilidades:

```text
proyecto/
├── datos/
│   ├── libros.txt          # 100 libros iniciales en formato texto separado por comas
│   └── socios.txt          # 15 socios iniciales en formato texto separado por comas
├── errores/
│   └── error.py            # Excepción personalizada DatosIncorrectos
├── modelo/
│   ├── libro.py            # Clase Libro (atributos y métodos propios de estado)
│   └── socio.py            # Clase Socio (atributos y métodos propios de préstamo)
├── almacenamiento.py       # Persistencia en ficheros (.txt) y registro de eventos (log.txt)
├── biblioteca.py           # Controlador con la lógica de negocio y validaciones
├── menu.py                 # Vista por consola (menú cíclico y captura de errores)
├── main.py                 # Punto de entrada y carga inicial de datos
└── log.txt                 # Archivo de auditoría con formato [Fecha][Evento][Detalles]
```

---

## Funcionalidades Implementadas

Al iniciar el programa, se cargan automáticamente los 100 libros y 15 socios desde sus respectivos ficheros `.txt`, mostrando una confirmación por consola antes de desplegar el menú cíclico:

1. **Mostrar lista de libros:** Muestra el catálogo completo en un formato legible indicando disponibilidad o socio asignado.
2. **Mostrar libros disponibles:** Filtra y muestra únicamente los libros libres (`cod_socio = None`).
3. **Buscar libro por título:** Permite buscar coincidencias parciales sin distinguir entre mayúsculas y minúsculas.
4. **Prestar libro:** Asocia un libro a un socio gestionando errores (libro ya prestado, socio con libro activo o códigos inexistentes) mediante la excepción personalizada `DatosIncorrectos`.
5. **Devolver libro:** Solicita el código del socio, libera el libro asignado y actualiza el estado de ambos.
6. **Mostrar socios con libro:** Lista únicamente los socios que tienen un ejemplar prestado actualmente junto con el título del libro.
7. **Añadir socios y libros:** Permite dar de alta nuevos registros validando datos obligatorios y formato de correo electrónico.
8. **Salir:** Vuelca el estado actual de libros y socios a los ficheros `.txt` antes de finalizar el programa.

---

## Requisitos Técnicos Cumplidos

* **POO y Métodos Propios:** Clases `Libro` y `Socio` con métodos personalizados no heredados (`esta_disponible()`, `prestar()`, `devolver()`, `tiene_libro()`, `tomar_libro()`, `devolver_libro()`).
* **Excepción Personalizada:** Clase `DatosIncorrectos(Exception)` con atributo de instancia `dato_erroneo`, capturada en bloques `try-except` para informar exactamente qué dato provocó el fallo.
* **Registro de Actividad (`log.txt`):** Trazabilidad de préstamos, devoluciones y altas con el formato `[Fecha][nombre del evento][detalles]`.
* **Dinámica de Trabajo con Git:** Desarrollo estructurado en rama `dev` y ramas por funcionalidad, integradas finalmente en `main` mediante Pull Request.

---

## Ejecución del Programa

1. Clonar el repositorio y situarse en la carpeta raíz del proyecto.
2. Ejecutar el archivo principal (requiere **Python 3.10+**):

```bash
python main.py
```

---

## Posibles Mejoras de la Aplicación

De cara a futuras versiones del sistema, se proponen las siguientes mejoras:

* **Préstamos múltiples por socio:** Modificar el atributo `cod_libro` de la clase `Socio` por una lista de códigos y establecer un límite configurable (por ejemplo, máximo 3 libros simultáneos por usuario).
* **Control de fechas y penalizaciones:** Añadir fecha de préstamo y fecha límite de devolución para calcular automáticamente retrasos y aplicar sanciones temporales.
* **Búsquedas avanzadas y filtrado:** Ampliar las consultas para permitir buscar libros por autor, categoría, año de publicación o disponibilidad combinada.
* **Edición y baja de registros:** Incorporar opciones en el menú para modificar datos de un libro o socio existente, así como dar de baja ejemplares descatalogados o socios inactivos.
* **Migración a base de datos relacional:** Sustituir los ficheros planos `.txt` por una base de datos **SQLite** para mejorar la integridad referencial y el rendimiento con grandes volúmenes de datos.
* **Interfaz gráfica o web:** Desarrollar una interfaz visual utilizando `Tkinter` o un entorno web ligero con `Flask` manteniendo intacta la capa de modelo y controlador actual.

[Video]{https://drive.google.com/file/d/1mwqikL0GFm2RhNKW3hCikZZUY9r_9-_3/view?usp=sharing}