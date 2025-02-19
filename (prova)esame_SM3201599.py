class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):       #! Potrei non aver messo def e aver scritto direttamente nella classe nel compito
        try:
            my_file = open(name, 'r') #verifico se file si può aprire con try except
        except:
            raise ExamException ('Errore: impossibile aprire il file')
        else:
            self.name = name  #!! più comodo
        my_file.close()

    def get_data (self):
        result = []
        my_file = open(self.name, 'r')
        c = 0
        for line in my_file:
            if c == 0:   #!! Salto prima riga OPPURE if elementi[0] != 'dt': (dopo elemento = line.split(',')
                c +=1
                continue
            elemento = line.split(',')
            temp = []  # creo lista temporanea dove mettiamo i due elementi della riga: data e media mensile
            media_mensile = int(elemento[1])
            if media_mensile > 0:
                temp.append (elemento[0])
                temp.append (media_mensile)  #aggiungo i due elementi alla lista temporanea
                result.append (temp)  #aggiungo lista temporanea a lista risulltato
        my_file.close()
        return result
    
time_series_file = CSVTimeSeriesFile(name = 'GlobalTemperatures.csv') #OPEN FOLDER PROGRAMMING LAB(cartella)
time_series = time_series_file.get_data()

def compute_variations (time_series, first_year, last_year, N):
    if not isinstance(first_year, int):
        raise ExamException ("First_year non è un intero")
    if not isinstance(last_year, int):
        raise ExamException ("last_year non è un intero")
    if not isinstance(N, int): #OPPURE if type(N) != int
        raise ExamException ("N non è un intero") #!! Ci assicuriamo che siano int

    if N >= last_year - first_year:
        raise ExamException ('Errore: lunghezza finestra intervallo troppo grande')
    diz_temp = {}
    for i in range (first_year, last_year + 1):
        diz_temp[i] = [] #!! Creo una lista per ogni chiave, ogni anno nella finestra
    for lista in time_series:
        anno = int(lista[0].split('-')[0])
        if anno >= first_year and anno <= last_year:
            diz_temp [anno].append(lista[1]) #il dizionario ha come chiave l'anno e come valore una lista di tutte le medie mensili di quell'anno

    diz_medie_annuali = {}
    for anno in diz_temp.keys():
        media_annuale = float(sommatoria(diz_temp[anno])) / float(len(diz_temp[anno]))  #!! Assicurati che sia float
        diz_medie_annuali [anno] = media_annuale #creo dizionario dove come chiave ha l'anno e come valore la sua media annuale
    
    diz_medie_mobili = {}  #!non credo che usavo cosi tanti dizionari nel compito
    for anno in range (first_year+N, last_year + 1):
        sum = 0
        for i in range (1,N+1):
            sum += diz_medie_annuali [anno-i]
        media_mobile = sum/N  #questo è sicuramente diverso da come ho fatto ma non mi ircordo come ho fatto al compito
        diz_medie_mobili [anno] = media_mobile
    
    diz_finale = {}
    for anno in range (first_year + N, last_year+1):
        diz_finale [str(anno)] = diz_medie_annuali[anno] - diz_medie_mobili[anno]

    return diz_finale

def sommatoria (lista):
    sum = 0
    for i in lista:
        sum += i
    return sum


def ControlloTemperatura (inf, sup, time_series):
    if not isinstance(inf, int):
        raise ExamException ("l'estremo inferiore+ non è un intero")
    if not isinstance(sup, int):
        raise ExamException ("l'estremo superiore non è un intero")

    lista_anni_abnormali = []
    for elemento in time_series:
        if elemento[1]<inf or elemento[1]>sup:
            anno = int(elemento[0].split("-")[0])
            if anno not in lista_anni_abnormali:
               lista_anni_abnormali.append(anno)
    return lista_anni_abnormali

print(compute_variations(time_series, 1901, 1904, 2))
print(ControlloTemperatura(123,125,time_series))




        


        
        

