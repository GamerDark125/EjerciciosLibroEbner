def raiz_n_esima(x, n):
    if n == 0:
        return "La raíz cero no está definida"
    resultado = x ** (1/n)
    return resultado

# Solicitar al usuario los valores de x y n
x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el valor de n (índice de la raíz): "))

# Calcular y mostrar la raíz n-ésima de x
resultado_raiz_n = raiz_n_esima(x, n)
print(f'La raíz {n}-ésima de {x} es: {resultado_raiz_n}')
