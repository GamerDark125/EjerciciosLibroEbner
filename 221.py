# Definir las listas a y b
a = [1, 2, 1]
b = [1, 2, 1]

# Verificar identidad de los primeros elementos
resultado_0 = a[0] is b[0]

# Verificar identidad de los segundos elementos
resultado_1 = a[1] is b[1]

# Verificar identidad de los terceros elementos
resultado_2 = a[2] is b[2]

# Verificar igualdad de las listas
igualdad_listas = a == b

# Verificar identidad de las listas
identidad_listas = a is b

# Mostrar resultados
print(resultado_0, resultado_1, resultado_2)
print(igualdad_listas)
print(identidad_listas)

# representacion grafica
#+---+     +-----+
#| a | --> | [1] | ----+
#+---+     +-----+     \
#                     +-----+
#+---+     +-----+ --> | [2] |
#| b | --> | [1] |     +-----+
#+---+     +-----+     /
#                     +-----+
#                     | [1] |
#                     +-----+
