def RigaDoppia (doc):
    with open (doc, "r") as file:
        RigaUnica = set(file.readlines())
        with open ("unique.txt", "w") as Uniquefile:
            Uniquefile.writelines (RigaUnica)
    print(Uniquefile)
