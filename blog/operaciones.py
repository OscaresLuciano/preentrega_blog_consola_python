
def listar_posts(lista):
    """
    Muestra el título y el nombre del autor de cada post.
    """
    print("\nLISTA DE POSTS:\n")

    for post in lista:
        # Verificamos que existan las claves antes de usarlas
        if (
            isinstance(post, dict)
            and "titulo" in post
            and "autor" in post
            and isinstance(post["autor"], dict)
            and "nombre" in post["autor"]
        ):
            print("-", post["titulo"], "| Autor:", post["autor"]["nombre"])
        else:
            print("- Post con datos incompletos (usá la opción 4 para validar)")


def buscar_por_titulo(lista, termino):
    """
    Busca publicaciones cuyo título contenga el término ingresado,
    sin distinguir mayúsculas de minúsculas.
    """
    termino = termino.strip().lower()

    if not termino:
        print("\nEl término de búsqueda no puede estar vacío")
        return []

    resultados = []

    for post in lista:
        if (
            isinstance(post, dict)
            and "titulo" in post
            and isinstance(post["titulo"], str)
            and termino in post["titulo"].lower()
        ):
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    """
    Busca publicaciones con una etiqueta que coincida exactamente
    con la ingresada, sin distinguir mayúsculas de minúsculas.
    """
    tag = tag.strip().lower()

    if not tag:
        print("\nLa etiqueta no puede estar vacía")
        return []

    resultados = []

    for post in lista:
        if (
            isinstance(post, dict)
            and "tags" in post
            and isinstance(post["tags"], list)
        ):
            for etiqueta in post["tags"]:
                if (
                    isinstance(etiqueta, str)
                    and tag == etiqueta.lower()
                ):
                    resultados.append(post)
                    break

    return resultados
