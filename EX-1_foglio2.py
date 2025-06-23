def ContaParola (doc, parola):
    c = 0
    with open (doc, 'r') as file:
        contenuto = file.read()
        parole = contenuto.split()
        for parol in parole:
            if parol == parola:
                c=c+1
    return c
