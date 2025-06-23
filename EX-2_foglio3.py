class Veicolo():
    def __init__ (self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.velocità = 0

    def __str__ (self):
        return 'veicolo "Modello {}, Marca {}, Anno{}, Velocità{}"'.format(self.modello, self.marca, self.anno, self.velocità)
    def accelerare (self):
        self.velocità += 5
    def frenare (self):
        self.velocità -= 5
    def get_speed (self):
        return self.velocità
    
class Auto(Veicolo):
        def __init__(self, modello, marca, numero_porte):
            super. __init__ (self, modello, marca)
            self.numero_porte = numero_porte
    
class Moto(Veicolo):
        def __init__(self, modello, marca, tipo):
            super. __init__ (self, modello, marca)
            self.tipo = tipo