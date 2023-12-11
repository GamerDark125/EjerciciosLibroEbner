def calcular_perimetro_triangulo():
    # Solicitar al usuario los lados del triángulo
    lado_a = float(input("Ingrese la longitud del lado a: "))
    lado_b = float(input("Ingrese la longitud del lado b: "))
    lado_c = float(input("Ingrese la longitud del lado c: "))

    # Calcular el perímetro
    perimetro = lado_a + lado_b + lado_c

    return perimetro

# Llamar a la función y mostrar el resultado
resultado = calcular_perimetro_triangulo()
print(f'El perímetro del triángulo es: {resultado}')
