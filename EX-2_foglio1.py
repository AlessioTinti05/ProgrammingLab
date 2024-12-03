def quante_volte (parola, lettera):
    count = 0
    for carattere in parola:
        if carattere == lettera:
            count = count + 1
    return count

print (quante_volte("arrosto", "a"))