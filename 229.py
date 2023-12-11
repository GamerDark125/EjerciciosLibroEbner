def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeros_primos(n):
    primos = [0] * n  # Inicializa un vector con n celdas nulas
    count = 0
    numero = 2

    while count < n:
        if es_primo(numero):
            primos[count] = numero
            count += 1
        numero += 1

    return primos

# Ejemplo de uso para obtener los primeros 5 números primos
n_primos = 5
resultado = primeros_primos(n_primos)
print(resultado)
