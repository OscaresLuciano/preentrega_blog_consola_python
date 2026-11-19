class Autor:
    def __init__(self, nombre, bio, especialidad=None, redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }


class Post:
    def __init__(self, id=None, titulo=None, contenido=None, autor=None, tags=None, estado=None):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, termino):
        termino = termino.strip().lower()

        if not termino:
            return []

        resultados = []

        for post in self.posts:
            if isinstance(post.titulo, str) and termino in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag):
        tag = tag.strip().lower()

        if not tag:
            return []

        resultados = []

        for post in self.posts:
            if isinstance(post.tags, list):
                for etiqueta in post.tags:
                    if isinstance(etiqueta, str) and tag == etiqueta.lower():
                        resultados.append(post)
                        break

        return resultados

    def crear_post(self, post):
        self.posts.append(post)

    def siguiente_id(self):
        mayor = 0

        for post in self.posts:
            if isinstance(post.id, int) and post.id > mayor:
                mayor = post.id

        return mayor + 1

    def validar_posts(self):
        from .validaciones import validar_post

        posts_validos = []

        for post in self.posts:
            print(f"\nValidando post {post.id}:")

            if validar_post(post):
                print("Resultado: válido")
                posts_validos.append(post)
            else:
                print("Resultado: inválido")

        return posts_validos

    def posts_a_diccionarios(self):
        lista = []

        for post in self.posts:
            lista.append(post.a_diccionario())

        return lista


def diccionario_a_autor(datos):
    return Autor(
        datos["nombre"],
        datos["bio"],
        datos.get("especialidad"),
        datos.get("redes_sociales")
    )


def diccionario_a_post(datos):
    return Post(
        datos["id"],
        datos["titulo"],
        datos["contenido"],
        diccionario_a_autor(datos["autor"]),
        datos["tags"],
        datos["estado"]
    )