def centigrados_a_farenheit(grados_centigrados):
    # Calcular grados Fahrenheit a partir de grados Celsius
    grados_farenheit = (grados_centigrados * 9/5) + 32
    return grados_farenheit

# Solicitar al usuario que ingrese la temperatura en grados Celsius
grados_centigrados = float(input("Ingrese la temperatura en grados Celsius: "))

# Calcular y mostrar la temperatura en grados Fahrenheit
resultado_farenheit = centigrados_a_farenheit(grados_centigrados)
print(f'{grados_centigrados} grados Celsius son {resultado_farenheit:.2f} grados Fahrenheit')
