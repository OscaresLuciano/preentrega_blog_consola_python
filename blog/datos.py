import json
from pathlib import Path

from .modelos import diccionario_a_post

BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_POSTS = BASE_DIR / "posts.json"

# Datos del autor
perfil_autor = {
    "nombre": "Edgar López",
    "bio": "Explorador de lugares exóticos",
    "especialidad": "Tecnología aplicada a viajes y turismo",
    "redes_sociales": ["@edgar_lopez", "@edgar_viaja"]
}

# Estados disponibles para los posts
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas disponibles en el blog
etiquetas_blog = {"Python", "Desarrollo", "Web", "IA"}


def cargar_posts():
    try:
        with open(ARCHIVO_POSTS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("Aviso: no existe posts.json. Se inicia con el blog vacío.")
        return []
    except ValueError:
        print("Aviso: posts.json está vacío o tiene contenido inválido. Se inicia con el blog vacío.")
        return []

    if not isinstance(datos, list):
        print("Aviso: posts.json no contiene una lista de posts. Se inicia con el blog vacío.")
        return []

    posts = []

    for diccionario in datos:
        try:
            posts.append(diccionario_a_post(diccionario))
        except (KeyError, TypeError):
            print("Aviso: se omitió un post con datos incompletos o inválidos.")

    return posts


def guardar_posts(blog):
    try:
        texto = json.dumps(blog.posts_a_diccionarios(), indent=4, ensure_ascii=False)
    except (TypeError, AttributeError):
        print("Error: hay datos que no se pueden convertir a JSON. No se guardó nada.")
        return False

    with open(ARCHIVO_POSTS, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    print("Posts guardados en posts.json")
    return True