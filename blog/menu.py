
def mostrar_menu():
    """
    Muestra el menú y retorna la opción elegida.
    Si la opción es inválida, muestra un mensaje y retorna None.
    """
    print("\n--- MENÚ DEL BLOG ---\n")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir\n")

    try:
        opcion = int(input("Elegí una opción: "))

        if opcion >= 1 and opcion <= 5:
            return opcion

        print("Opción incorrecta. Elegí una opción del 1 al 5")
        return None

    except ValueError:
        print("Error: ingresá un número")
        return None
