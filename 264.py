def farenheit_a_centigrados(grados_farenheit):
    # Calcular grados centígrados a partir de grados Farenheit
    grados_centigrados = (grados_farenheit - 32) * 5/9
    return grados_centigrados

# Solicitar al usuario que ingrese la temperatura en grados Farenheit
grados_farenheit = float(input("Ingrese la temperatura en grados Farenheit: "))

# Calcular y mostrar la temperatura en grados centígrados
resultado_centigrados = farenheit_a_centigrados(grados_farenheit)
print(f'{grados_farenheit} grados Farenheit son {resultado_centigrados:.2f} grados centígrados')
