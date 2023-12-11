import math

def area_circulo(radio):
    # Calcular el área del círculo usando la fórmula πr^2
    area = math.pi * radio**2
    return area

# Ejemplo de uso
radio_circulo = 5
resultado_area = area_circulo(radio_circulo)
print(f'El área del círculo con radio {radio_circulo} es: {resultado_area}')
