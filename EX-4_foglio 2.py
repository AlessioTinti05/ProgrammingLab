def PrimaParola(doc):
    with open(doc, "r") as file:
        diz = {}
        contenuto = file.read()
        # Sostituisco ! e ? con .
        contenuto = contenuto.replace('!', '.').replace('?', '.').replace(',','.')
        frasi = contenuto.split('.')
        for frase in frasi:
            parole = frase.split()
            if parole:
                puntofirst = parole[0]
                if puntofirst not in diz:
                    diz[puntofirst] = 1
                else:
                    diz[puntofirst] += 1
    print(diz)