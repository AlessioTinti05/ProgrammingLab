def RigaDoppia(doc):
    righe_uniche = []
    viste = set()

    with open(doc, "r") as file:
        for line in file:
            if line not in righe_uniche:
                righe_uniche.append(line)

    with open("unique.txt", "w") as nuovo_file:
        nuovo_file.writelines(righe_uniche)
