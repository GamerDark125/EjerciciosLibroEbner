def es_perfecto(num):
    sumatorio = sum(i for i in range(1, num // 2 + 1) if num % i == 0)
    return sumatorio == num

def numeros_perfectos_hasta_n(n):
    return [i for i in range(2, n + 1) if es_perfecto(i)]

# Solicitar al usuario que ingrese el valor de n
n = int(input("Ingrese un número entero n: "))

# Obtener la lista de números perfectos hasta n
lista_perfectos = numeros_perfectos_hasta_n(n)

# Mostrar la lista de números perfectos
print(f'Números perfectos hasta {n}: {lista_perfectos}')
