def mostrar_menu():
    # Función para mostrar el menú de opciones al usuario.
    print("Lista de Compras")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Ver lista de compras")
    print("4. Salir")
    print()

def agregar_elemento(lista):
    # Función para agregar un elemento a la lista de compras.
    elemento = input("Ingrese el nombre del elemento a agregar: ")
    lista.append(elemento)
    print(f"{elemento} ha sido agregado a la lista.")

def eliminar_elemento(lista):
    # Función para eliminar un elemento de la lista de compras.
    if not lista:
        print("La lista de compras está vacía.")
        return

    print("Lista de compras:")
    for index, elemento in enumerate(lista, 1):
        print(f"{index}. {elemento}")

    try:
        numero_elemento = int(input("Ingrese el número del elemento que desea eliminar: "))
        if 1 <= numero_elemento <= len(lista):
            elemento_eliminado = lista.pop(numero_elemento - 1)
            print(f"{elemento_eliminado} ha sido eliminado de la lista.")
        else:
            print("Número de elemento inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def ver_lista(lista):
    # Función para mostrar la lista de compras completa.
    if not lista:
        print("La lista de compras está vacía.")
    else:
        print("Lista de compras:")
        for elemento in lista:
            print(f"- {elemento}")

def main():
    # Función principal del programa.
    lista_compras = []

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción que desea ejecutar: ")

        if opcion == "1":
            agregar_elemento(lista_compras)
        elif opcion == "2":
            eliminar_elemento(lista_compras)
        elif opcion == "3":
            ver_lista(lista_compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida (1, 2, 3 o 4).")

if __name__ == "__main__":
    main()
