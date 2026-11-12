
from .datos import estados_post


def validar_post(post):
    """
    Comprueba que una publicación tenga todos los campos
    obligatorios y que sus datos sean válidos.

    Retorna True si el post es válido y False si no lo es.
    """
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    if not isinstance(post, dict):
        print("Error: el post debe ser un diccionario")
        return False

    for clave in claves_obligatorias:
        if clave not in post:
            print(f"Error: falta la clave '{clave}'")
            return False

    if not isinstance(post["titulo"], str) or not isinstance(post["contenido"], str):
        print("Error: el título y el contenido deben ser textos")
        return False

    if not post["titulo"].strip() or not post["contenido"].strip():
        print("Error: falta el título o el contenido")
        return False

    if not isinstance(post["tags"], list):
        print("Error: las etiquetas deben ser una lista")
        return False

    for etiqueta in post["tags"]:
        if not isinstance(etiqueta, str):
            print("Error: todas las etiquetas deben ser textos")
            return False

    if not isinstance(post["autor"], dict) or "nombre" not in post["autor"]:
        print("Error: el autor debe ser un diccionario y tener la clave 'nombre'")
        return False

    if not isinstance(post["autor"]["nombre"], str):
        print("Error: el nombre del autor debe ser un texto")
        return False

    if not post["autor"]["nombre"].strip():
        print("Error: el nombre del autor no puede estar vacío")
        return False

    if post["estado"] not in estados_post:
        print(f"Error: estado inválido. Estados permitidos: {estados_post}")
        return False

    return True
