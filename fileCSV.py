
class CSVfile ():
    def __init__ (self, name):
        self.name = name

    def get_data (self):
        data = []
        with open (self.name, "r") as file:
            for line in file:
                try:
                    data.append(line.split(","))
                except Exception as e:
                    return ('Errore! {}'.format (e))
        if self.name is not str in  super.__init__():
            raise Exception ("Errore. il nome inserito non è valido")
        return data
    
class NumericalCSVfile (CSVfile):
    def __init__ (self, name):
        super.__init__(self, name)
    
    def get_data(self):
        data = super.get_data(self)
        for elemento in data:
            for elemento in elemento:
                try:
                    data.append(float(elemento.split(",")))
                except:
                    data.append(elemento.split(","))
        return data
#Onestamente sta roba dei testing non l'ho ben capita
