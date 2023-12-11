import math

def grados_a_radianes(grados):
    # Calcular radianes a partir de grados usando la fórmula π/180
    radianes = grados * (math.pi / 180)
    return radianes

# Solicitar al usuario que ingrese la cantidad de grados
grados = float(input("Ingrese la cantidad de grados: "))

# Calcular y mostrar la cantidad en radianes
resultado_radianes = grados_a_radianes(grados)
print(f'{grados} grados son {resultado_radianes:.2f} radianes')
