import math

def logaritmo_en_base(b, x):
    if b <= 0 or b == 1 or x <= 0:
        # Manejar casos donde b <= 0, b == 1, o x <= 0
        return "Valores no válidos para el logaritmo"
    
    resultado = math.log(x, b)
    return resultado

# Solicitar al usuario los valores de b y x
base = float(input("Ingrese el valor de b (base del logaritmo): "))
numero = float(input("Ingrese el valor de x (argumento del logaritmo): "))

# Calcular el logaritmo en base b de x y mostrar el resultado
resultado_logaritmo = logaritmo_en_base(base, numero)
print(f'El logaritmo en base {base} de {numero} es: {resultado_logaritmo}')
