lista = ['Pepe', 'Juan', 'María', 'Ana', 'Luis', 'Pedro']

for i in range(1, len(lista)):
    for j in range(0, len(lista)-i):
        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento

print(lista)
