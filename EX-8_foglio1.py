def trascrizione (lista):
    lista2 = []
    for item in lista:
        if (item == 0):
            item = "Zero"
            lista2.append(item)
        if (item == 1):
            item = "Uno"
            lista2.append(item)
        if (item == 2):
            item = "Due"
            lista2.append(item)
        if (item == 3):
            item = "Tre"
            lista2.append(item)
        if (item == 4):
            item = "Quattro"
            lista2.append(item)
        if (item == 5):
            item = "Cinque"
            lista2.append(item)
        if (item == 6):
            item = "Sei"
            lista2.append(item)
        if (item == 7):
            item = "Sette"
            lista2.append(item)
        if (item == 8):
            item = "Otto"
            lista2.append(item)
        if (item == 9):
            item = "Nove"
            lista2.append(item)
    return lista2


list = [1, 2, 3, 4, 5, 6, 7, 9, 8]
print(trascrizione(list))
        