from .datos import estados_post
from .modelos import Autor, Post
from .validaciones import validar_post


def mostrar_posts(lista):
    """
    Muestra título, autor y estado de cada post de la lista.
    """
    if not lista:
        print("\nNo hay posts para mostrar")
        return

    print("\nLISTA DE POSTS:\n")
    for post in lista:
        print(f"- {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")


def pedir_texto(mensaje):
    """
    Pide un texto al usuario y lo vuelve a pedir si queda vacío.
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: este campo no puede quedar vacío")


def pedir_estado():
    """
    Pide el estado del post y lo vuelve a pedir si no es uno de los permitidos.
    """
    print("Estados posibles:", ", ".join(estados_post))
    while True:
        estado = pedir_texto("Estado: ").lower()
        if estado in estados_post:
            return estado
        print("Error: estado no válido")


def pedir_tags():
    """
    Pide las etiquetas separadas por comas y las devuelve como lista.
    """
    while True:
        texto = pedir_texto("Etiquetas (separadas por comas): ")
        tags = []
        for etiqueta in texto.split(","):
            etiqueta = etiqueta.strip().lower()
            if etiqueta:
                tags.append(etiqueta)
        if tags:
            return tags
        print("Error: ingresá al menos una etiqueta")


def crear_post_desde_consola(blog):
    """
    Pide los datos por consola, crea los objetos Autor y Post
    y agrega el post al blog si es válido.
    """
    print("\nNUEVO POST\n")
    titulo = pedir_texto("Título: ")
    contenido = pedir_texto("Contenido: ")
    tags = pedir_tags()
    estado = pedir_estado()

    nombre_autor = pedir_texto("Nombre del autor: ")
    bio_autor = pedir_texto("Bio del autor: ")

    autor = Autor(nombre_autor, bio_autor)
    post = Post(blog.siguiente_id(), titulo, contenido, autor, tags, estado)

    if validar_post(post):
        blog.crear_post(post)
        print(f"\nPost creado con id {post.id}. Recordá guardar (opción 6).")
    else:
        print("\nNo se pudo crear el post")