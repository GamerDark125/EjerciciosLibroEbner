def comprueba_letra_dni(numero_dni, letra):
    letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'

    # Verificar que el número de DNI sea un entero positivo
    if not isinstance(numero_dni, int) or numero_dni <= 0:
        return False

    # Calcular la letra correspondiente al número de DNI
    letra_calculada = letras_validas[numero_dni % 23]

    # Comparar la letra calculada con la letra proporcionada
    return letra_calculada == letra

# Solicitar al usuario el número de DNI y la letra
numero_dni_input = input("Ingrese el número de DNI: ")
letra_input = input("Ingrese la letra del DNI: ")

try:
    numero_dni = int(numero_dni_input)
    # Convertir la letra a mayúsculas para asegurar la comparación
    letra = letra_input.upper()

    # Llamar a la función y mostrar el resultado
    resultado = comprueba_letra_dni(numero_dni, letra)
    print(f'¿La letra {letra} corresponde al número de DNI {numero_dni}? {resultado}')
except ValueError:
    print("Por favor, ingrese un número de DNI válido.")
