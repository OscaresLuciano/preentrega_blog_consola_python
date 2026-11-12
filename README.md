# Sistema de Blog por Consola

Proyecto desarrollado en Python para el curso de Coderhouse, correspondiente a la Preentrega 5.

## Descripción

El programa permite gestionar y consultar publicaciones de un blog desde la consola. Se utiliza una estructura modular para separar los datos, las operaciones, las validaciones y el menú principal.

## Funcionalidades

- Listar publicaciones y sus autores.
- Buscar publicaciones por título.
- Filtrar publicaciones por etiqueta.
- Validar los datos de cada publicación.
- Manejar opciones incorrectas del menú sin finalizar el programa.

## Estructura del proyecto

```text
preentrega_clase_5/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

- **main.py:** inicia el programa y conecta los distintos módulos.
- **datos.py:** contiene los datos del autor y las publicaciones.
- **menu.py:** muestra el menú y procesa la opción ingresada.
- **operaciones.py:** contiene las funciones para listar, buscar y filtrar publicaciones.
- **validaciones.py:** comprueba que los posts tengan los datos requeridos.
- **__init__.py:** permite organizar los módulos dentro del paquete `blog`.

## Cómo ejecutar el programa

Se necesita tener Python 3 instalado.

Desde una terminal, ubicarse en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

El programa mostrará un menú con cinco opciones. Se puede utilizar hasta seleccionar la opción de salir.

## Tecnologías utilizadas

- Python 3
- Módulos y paquetes de Python
- Listas, diccionarios, tuplas y conjuntos
- Funciones, condicionales y manejo de excepciones

## Autor

Luciano

Proyecto realizado para el curso de Python de Coderhouse.