import math

def radianes_a_grados(radianes):
    # Calcular grados a partir de radianes usando la fórmula 180/π
    grados = radianes * (180 / math.pi)
    return grados

# Solicitar al usuario que ingrese la cantidad de radianes
radianes = float(input("Ingrese la cantidad de radianes: "))

# Calcular y mostrar la cantidad en grados
resultado_grados = radianes_a_grados(radianes)
print(f'{radianes} radianes son {resultado_grados:.2f} grados')
