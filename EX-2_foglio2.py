def ContaParole (doc):
    with open (doc, 'r') as file:
        diz = {}
        contenuto = file.read()
        words = contenuto.split()
        for word in words:
            count = contenuto.count(word)
            diz ['word'] = count
    print(diz)

def ContaParol2e (doc):
    with open (doc, 'r') as file:
        diz = {}
        contenuto = file.read()
        words = contenuto.split()
        for word in words:
            if word not in diz.keys():
                diz[word] = 1
            else:
                diz[word] += 1
        return diz
            