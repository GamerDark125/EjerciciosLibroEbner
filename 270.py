def calcular_letra_dni(numero_dni):
    # Obtener el resto al dividir el número por 23
    resto = numero_dni % 23

    # Definir la tabla de letras correspondientes a cada resto
    letras_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'

    # Obtener la letra correspondiente al resto
    letra = letras_dni[resto]

    return letra

# Solicitar al usuario que ingrese el número de DNI
numero_dni = int(input("Ingrese el número de DNI (sin la letra): "))

# Calcular y mostrar la letra correspondiente al número de DNI
letra_dni = calcular_letra_dni(numero_dni)
print(f'La letra correspondiente al número {numero_dni} es: {letra_dni}')
