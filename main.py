
from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Ingresá el título a buscar: ")
            resultados = buscar_por_titulo(posts, termino)

            if resultados:
                for post in resultados:
                    print("\nPost encontrado:", post["titulo"])
            else:
                print("\nNo se encontraron resultados para la búsqueda")

        elif opcion == 3:
            tag = input("Ingresá el tag a buscar: ")
            resultados = filtrar_por_tag(posts, tag)

            if resultados:
                for post in resultados:
                    print("\nPost encontrado:", post["titulo"])
            else:
                print("\nNo se encontraron resultados para la búsqueda")

        elif opcion == 4:
            for post in posts:
                if isinstance(post, dict) and "id" in post:
                    print(f"\nValidando post {post['id']}:")
                else:
                    print("\nValidando post sin ID:")

                resultado = validar_post(post)
                print("Resultado:", resultado)

        elif opcion == 5:
            print("\n¡Hasta luego!")
            break
