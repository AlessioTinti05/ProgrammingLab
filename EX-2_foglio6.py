def quadrat (valore):
    valore = input("Inserisci un valore \n")
    if type(valore) != int:
        raise Exception("Input non valido, devi inserire un numero intero, hai inseiro il tipo {}".format(type(valore)))
    else:
        valore = valore*valore
        return valore