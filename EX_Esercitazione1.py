class ExamException (Exception):
    pass

class MovingAverage ():
    def __init__(self, window):
        self.window = window
    
    def compute(self, data):
        self.result_list = []
        self.data = data
        a = 0
        b = self.window
        for i in range (0, (len(data) - self.window)):
            for i in range (a,b):
                sum = 0
                temp = data[a:b]
                for item in temp:
                    sum = sum + item
                avg = sum/self.window
            self.result_list.append(avg)
            a = a+1
            b = b+1
        return self.result_list
    
p = int(input ("definisci la lunghezza della finestra:"))
if (p <=0):
    raise ExamExcepton ("Numero non valido. Hai inserito un numero negativo o nullo")
moving_avg = MovingAverage(p)
l = int(input("Definisci la lunghezza della lista:"))
if (l <=0):
    raise ExamExcepton ("Numero non valido. Hai inserito un numero negativo o nullo")
if (l < p):
    raise ExamExcepton ("Numero non valido. La finestra delle media mobile non puo essere piu grande della lunghezza della lista")
lista = []
for i in range (0,l):
    a = int(input ("inserisci l'elemento della lista"))
    if type (a) is not int:
        raise ExamExcepton ("Bisogna inserire un numero intero")
    lista.append(a)
result = moving_avg.compute([2,4,8,16])
print(result)




