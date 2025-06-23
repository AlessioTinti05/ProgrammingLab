class ExamException(Exception):
    pass
class MovingAverage:
    def __init__ (self, len):
        self.len = len

    def compute(self, lista):
        self.lista = lista
        self.lenlista = len(lista)
        if ( self.len <= 0):
            raise ExamException ("Lunghezza finestra non valida")
        if ( self.lenlista<=0 ):
            raise ExamException ("Lunghezza lista più piccola della lunghezza della finestra")
        if ( self.lenlista < self.len):
            raise ExamException ("Lunghezza lista più piccola della lunghezza della finestra")
        i = 0
        j = self.len -1
        result = []
        while (j < self.lenlista):
            somma = 0
            for u in range(0, self.len):
                somma = somma + lista[u+i]
            result.append(somma/self.len)
            i = i+1
            j=j+1
        return result

movingavg = MovingAverage(3)
result = movingavg.compute([1,2,3,4,5,6])
print(result)
