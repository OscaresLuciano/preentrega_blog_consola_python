
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

# Lista de publicaciones
posts = [
    {
        "id": 1,
        "titulo": "Introducción a Python",
        "contenido": "Python es un lenguaje simple y poderoso.",
        "autor": perfil_autor,
        "tags": ["python", "programacion", "tutorial"],
        "estado": "publicado",
    },
    {
        "id": 2,
        "titulo": "Primeros pasos con Django",
        "contenido": "Django es un framework web para Python.",
        "autor": perfil_autor,
        "tags": ["django", "python"],
        "estado": "borrador",
    },
    {
        # Post incompleto a propósito
        "id": 3,
        "titulo": "Análisis de datos",
        "autor": perfil_autor,
        "tags": ["datos"],
        "estado": "publicado",
    },
    {
        # Post con tipos de datos incorrectos
        "id": 4,
        "titulo": "Post con errores",
        "contenido": "Este post tiene tipos de datos incorrectos.",
        "autor": perfil_autor,
        "tags": "python",
        "estado": "eliminado",
    }
]
