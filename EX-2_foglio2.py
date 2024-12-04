def ContaParole (doc):
    with open (doc, 'r') as file:
        diz = {}
        contenuto = file.read()
        words = contenuto.split()
        for word in words:
            count = contenuto.count(word)
            diz ['word'] = count
    print(diz)