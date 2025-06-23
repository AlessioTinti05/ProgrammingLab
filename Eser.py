class Veicolo:
    def __init__ (self, modello, marca, anno):
        self.modello = modello
        self.marca=marca
        self.anno=anno
        self.speed=0
    def __str__(self):
        return ("Modello: {}. Marca: {}. Anno: {}. Velocità: {}.".format(self.modello, self.marca, self.anno, self.speed))
    def accelerare (self):
        self.speed = self.speed + 5
        return self
    def frenare (self):
        self.speed = self.speed - 5
        return self
    def get_speed (self):
        return self.speed
    
x = Veicolo("Fiat", "Fiat2", 3000)
print(x)

class Auto(Veicolo):
    def __init__ (self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte
    def __str__ (self):
        return ("{} Numero_porte: {}".format(super().__str__(), self.numero_porte))

y = Auto("Panda", "adnaP", 2089, 4)
print(y)

class Moto(Veicolo):
    def __init__ (self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo
    def __str__ (self):
        return ("{} Tipo: {}".format(super().__str__(), self.tipo))
    
z = Moto("Iamahah", "hahamaI", 3, "Sportivvvv")
print(z)