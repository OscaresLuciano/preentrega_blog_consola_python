from .datos import estados_post
from .modelos import Autor, Post


def validar_post(post):
    if not isinstance(post, Post):
        print("Error: la publicación debe ser un objeto Post")
        return False

    if post.id is None:
        print("Error: falta el id de la publicación")
        return False

    if not isinstance(post.titulo, str) or not isinstance(post.contenido, str):
        print("Error: el título y el contenido deben ser textos")
        return False

    if not post.titulo.strip() or not post.contenido.strip():
        print("Error: falta el título o el contenido")
        return False

    if not isinstance(post.tags, list):
        print("Error: las etiquetas deben ser una lista")
        return False

    for etiqueta in post.tags:
        if not isinstance(etiqueta, str):
            print("Error: todas las etiquetas deben ser textos")
            return False

    if not isinstance(post.autor, Autor):
        print("Error: el autor debe ser una instancia de Autor")
        return False

    if not isinstance(post.autor.nombre, str) or not post.autor.nombre.strip():
        print("Error: el nombre del autor no puede estar vacío")
        return False

    if post.estado not in estados_post:
        print("Error: el estado de la publicación no es válido")
        return False

    return True