def ParolaMaxPerLettera (doc):
    with open (doc, "r") as file:
        contenuto = file.read()
        words = contenuto.split()
        alfabeto = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        lettere = alfabeto.split()
        diz = {}
        for lettera in alfabeto:
            max = "i"
            for word in file:
                if len(word) > len(max):
                    max = word
            diz [lettera] = word
        print (diz)