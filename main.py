from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog.modelos import Blog
from blog.operaciones import mostrar_posts, crear_post_desde_consola


def main():
    blog = Blog(cargar_posts())

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            mostrar_posts(blog.listar_posts())

        elif opcion == 2:
            termino = input("Ingresá el título a buscar: ")
            resultados = blog.buscar_por_titulo(termino)

            if resultados:
                mostrar_posts(resultados)
            else:
                print("\nNo se encontraron resultados para la búsqueda")

        elif opcion == 3:
            tag = input("Ingresá el tag a buscar: ")
            resultados = blog.filtrar_por_tag(tag)

            if resultados:
                mostrar_posts(resultados)
            else:
                print("\nNo se encontraron resultados para la búsqueda")

        elif opcion == 4:
            crear_post_desde_consola(blog)

        elif opcion == 5:
            validos = blog.validar_posts()
            print(f"\nPosts válidos: {len(validos)} de {len(blog.listar_posts())}")

        elif opcion == 6:
            guardar_posts(blog)

        elif opcion == 7:
            respuesta = input("¿Guardar los cambios antes de salir? (s/n): ").strip().lower()
            if respuesta == "s":
                guardar_posts(blog)
            print("\n¡Hasta luego!")
            break


if __name__ == "__main__":
    main()