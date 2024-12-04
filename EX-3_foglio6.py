def scelta (input):
    while true:
        input = input("Scegli: 1 per sommare, 2 per sottrarre, 3 per uscire")
        for input in {"1", "2", "3"}:
            if input == "1":
                valore1 = input("Scegli il primo numero: \n")
                valore2 = input ("Scegli il secondo valore: \n")
                print (valore1 + valore2)
                input = input("Scegli: 1 per sommare, 2 per sottrarre, 3 per uscire")
            elif input == "2":
                valore1 = input("Scegli il primo numero: \n")
                valore2 = input ("Scegli il secondo valore: \n")
                print (valore1 - valore2)
                input = input("Scegli: 1 per sommare, 2 per sottrarre, 3 per uscire")
            elif input == "3":
                return ("Grazie per aver giocato")
            else:
                raise Exception ("Scelta non valida. hai inserito {}, devi inserire 1, 2 o 3".format(input))