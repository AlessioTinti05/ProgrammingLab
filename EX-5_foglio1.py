def scambia(lista, i, j):
    k = lista[i]
    lista[i] = lista[j]
    lista[j] = k
    return lista
list = [1, 2, 5, 6, 8]
print(scambia(list, 3, 4))