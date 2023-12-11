def menu_generico(opciones):
    while True:
        print("Menú:")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

        try:
            seleccion = int(input("Seleccione una opción (1-{0}): ".format(len(opciones))))
            if 1 <= seleccion <= len(opciones):
                return seleccion
            else:
                print(f"Error: Seleccione un número entre 1 y {len(opciones)}.\n")
        except ValueError:
            print("Error: Ingrese un número válido.\n")

# Ejemplo de uso
opciones_menu = ["Ingresar dinero", "Sacar dinero", "Consultar saldo"]
eleccion = menu_generico(opciones_menu)
print(f'Ha elegido la opción: {eleccion}')
