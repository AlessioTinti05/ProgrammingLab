class utente ():
    def __init__ (self, name, ora, minuto, secondo, giorno, mese, anno):
        self.name = name
        self.ora = ora
        self.minuto = minuto
        self.secondo = secondo
        self.giorno = giorno
        self.mese =mese
        self.anno=anno
        
    def compleanno (self):
        self.ora = input()
        self.minuto = input()
        self.secondo = input ()
        self.giorno = input()
        self.mese = input()
        self.anno = input()

        annoC = 2024
        meseC = 12
        giornoC = 4
        oraC = 9
        minutoC = 57
        secondoC = 21

        differenza = []
        differenza.append ( annoC - self.anno)
        differenza.append (meseC - self.mese)
        differenza.append (giornoC - self.giorno)
        differenza.append (oraC - self.ora)
        differenza.append (minutoC - self.minuto)
        differenza.append (secondoC - self.secondo)
        return differenza
