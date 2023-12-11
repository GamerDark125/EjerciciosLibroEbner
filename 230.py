def leer_lista_positiva():
    lista = []
    intentos_maximos = 3

    for _ in range(10):
        for intento in range(1, intentos_maximos + 1):
            try:
                numero = int(input(f"Ingrese un número positivo (intento {intento}): "))
                if numero >= 0:
                    lista.append(numero)
                    break
                else:
                    print("Error: El número ingresado es negativo. Inténtelo de nuevo.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

        else:
            print(f"Ha excedido el número máximo de intentos ({intentos_maximos}). Terminando programa.")
            return None

    return lista

# Ejemplo de uso
lista_positiva = leer_lista_positiva()

if lista_positiva is not None:
    print("Lista de números positivos:", lista_positiva)
