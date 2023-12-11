import random

def numero_aleatorio_entre_10():
    return random.uniform(-10.0, 10.0)

# Ejemplo de uso
resultado_entre_10 = numero_aleatorio_entre_10()
print(f'Número aleatorio entre -10.0 y 10.0: {resultado_entre_10}')
