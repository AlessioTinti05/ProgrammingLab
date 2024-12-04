def scelta (input):
    input = input("Scegli: 1 per sommare, 2 per sottrarre, 3 per uscire")
    for input in {"1", "2", "3"}:
        if input == 1:
            valore1 = input("Scegli il primo numero: \n")
            valore2 = input ("Scegli il secondo valore: \n")
            print (valore1 + valore2)
        elif input == 2:
            valore1 = input("Scegli il primo numero: \n")
            valore2 = input ("Scegli il secondo valore: \n")
            print (valore1 - valore2)
        elif input == 3:
            return ("Grazie per aver giocato")
