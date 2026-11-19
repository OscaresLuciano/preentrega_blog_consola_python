# Blog por consola - Preentrega 6: POO y persistencia JSON

Sistema de blog que funciona por consola. Permite ver, buscar, filtrar, crear y validar publicaciones, y guardarlas en un archivo `posts.json` para que se conserven entre ejecuciones.

## Cómo ejecutarlo

Desde la carpeta del proyecto:

    python main.py

(En algunos sistemas: `python3 main.py`)

## Estructura del proyecto

    preentrega_blog_consola_python/
    ├── main.py            -> punto de entrada: carga datos, crea el Blog y maneja el menú
    ├── posts.json         -> archivo donde se guardan los posts
    ├── README.md
    └── blog/
        ├── __init__.py    -> convierte la carpeta en un paquete
        ├── datos.py       -> carga y guardado de posts.json, estados permitidos
        ├── menu.py        -> muestra el menú y lee la opción elegida
        ├── modelos.py     -> clases Autor, Post y Blog
        ├── operaciones.py -> funciones de consola: mostrar posts y crear un post nuevo
        └── validaciones.py-> validación de los datos de un post

## Clases principales (blog/modelos.py)

- **Autor**: representa a la persona que escribe. Atributos: `nombre`, `bio`, `especialidad` y `redes_sociales`.
- **Post**: representa una publicación. Atributos: `id`, `titulo`, `contenido`, `autor`, `tags` y `estado`. El atributo `autor` es un objeto `Autor` (composición), no un texto.
- **Blog**: centraliza la lógica del sistema. Tiene una lista de objetos `Post` y métodos para:
  - `listar_posts()`: devuelve todos los posts.
  - `buscar_por_titulo(termino)`: busca sin distinguir mayúsculas y minúsculas.
  - `filtrar_por_tag(tag)`: filtra sin distinguir mayúsculas y minúsculas.
  - `crear_post(post)`: agrega un post nuevo.
  - `siguiente_id()`: calcula el id para un post nuevo.
  - `validar_posts()`: valida cada post usando `validaciones.py`.
  - `posts_a_diccionarios()`: convierte todos los posts a diccionarios para guardarlos.

## Cómo se guarda y carga la información

JSON no puede guardar objetos de Python directamente, por eso se convierten:

- **Al guardar**: cada objeto se convierte a diccionario con su método `a_diccionario()`. El `Post` también le pide a su `Autor` que se convierta. Después `guardar_posts()` (en `datos.py`) escribe la lista de diccionarios en `posts.json`.
- **Al cargar**: al iniciar el programa, `cargar_posts()` lee `posts.json` y reconstruye cada objeto con `diccionario_a_post()` y `diccionario_a_autor()`. Con esa lista de objetos se crea el `Blog`.

## Manejo de errores

- Si `posts.json` no existe, está vacío o tiene contenido inválido, se muestra un aviso y el blog arranca vacío, sin cerrarse.
- Si un post del archivo tiene datos incompletos, se omite con un aviso y se cargan los demás.
- Si algún dato no se puede convertir a JSON, no se guarda nada y no se pierde el archivo anterior.
- Las opciones inválidas del menú y los campos vacíos al crear un post muestran un mensaje de error y se vuelven a pedir.

El `posts.json` incluido tiene dos posts con errores a propósito, para probar estos casos: el post 3 (sin contenido) se omite al cargar y el post 4 (etiquetas y estado inválidos) aparece como inválido en la opción 5.

## Menú

    1. Ver todos los posts
    2. Buscar por título
    3. Filtrar por tag
    4. Crear nuevo post
    5. Validar posts
    6. Guardar posts en JSON
    7. Salir (pregunta si se quieren guardar los cambios)

## Cambios respecto a la preentrega anterior

- Se agregó `blog/modelos.py` con las clases `Autor`, `Post` y `Blog`.
- Los posts y autores pasaron de ser diccionarios a ser objetos.
- La búsqueda y el filtrado ahora son métodos de la clase `Blog`.
- `datos.py` ya no tiene la lista de posts escrita en el código: ahora los carga y los guarda en `posts.json`.
- Se agregaron las opciones para crear un post nuevo y guardar en JSON.
- `validaciones.py` ahora valida objetos `Post` en lugar de diccionarios.
- `main.py` crea una instancia de `Blog` y llama a sus métodos.