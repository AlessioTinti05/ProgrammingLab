def scelta():
    while True:
        scelta = input("Scegli: 1 per sommare, 2 per sottrarre, 3 per uscire\n")
        if scelta == "1":
            valore1 = float(input("Scegli il primo numero: \n"))
            valore2 = float(input("Scegli il secondo valore: \n"))
            print("Risultato:", valore1 + valore2)
        elif scelta == "2":
            valore1 = float(input("Scegli il primo numero: \n"))
            valore2 = float(input("Scegli il secondo valore: \n"))
            print("Risultato:", valore1 - valore2)
        elif scelta == "3":
            print("Grazie per aver giocato")
            break
        else:
            print(f"Scelta non valida. Hai inserito {scelta}, devi inserire 1, 2 o 3.")
