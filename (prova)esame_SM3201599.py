class ExamException(Exception):
    pass
class CSVTimeSeriesFile ():
    def __init__(self, name):       #! Potrei non aver messo def e aver scritto direttamente nella classe nel compito
        self.name = name
        try:
            my_file = open(self.name, 'r') #verifico se file si può aprire con try except
        except:
            raise ExamException ('Errore: impossibile aprire il file')
        my_file.close
    def get_data (self):
        result = []
        my_file = open(self.name, 'r')
        for line in my_file:
            elemento = line.split(',')
            temp = []  # creo lista temporanea dove mettiamo i due elementi della rig: data e media mesile
            temp.append (elemento[0]) 
            media_mensile = int(elemento[1])
            if media_mensile <= 0:
                raise ExamException ('Errore: valore media mensile non valido')
            temp.append (media_mensile)  #aggiungo i due elementi alla lista temporanea
            result.append (temp)  #aggiungo lista temporanea a lista risulltato
        return result
    
time_series_file = CSVTimeSeriesFile(name = 'GlobalTemperatures.csv') #? file csv è nella stessa cartella, perché non funziona? (Errore impossibile aprire file)
time_series = time_series_file.get_data()

def compute_variations (time_series, first_year, last_year, N):
    first_year = int(first_year)
    last_year = int(last_year) # Ci assicuriamo che siano int
    if N >= last_year - first_year:
        raise ExamException ('Errore: lunghezza finestra intervallo troppo grande')
    diz_temp = {}
    for lista in time_series:
        temp_list = []
        anno = lista.split('-')[0]
        for anno in lista:
            temp_list.append(time_series[1]) #alla lista temporanea aggiungo via via tutte le medie mensili di un anno
        diz_temp [anno] = temp_list #il dizionario ha come chiave l'anno e come valore una lista di tutte le medie mensili di quell'anno
    
    diz_medie_annuali = {}
    for anno in diz_temp.keys:
        media_annuale = sum(diz_temp [anno]) / len(diz_temp [anno])
        diz_medie_annuali [anno] = media_annuale #creo dizionario dove come chiave ha l'anno e come valore la sua media annuale
    
    diz_medie_mobili = {}  #!non credo che usavo cosi tanti dizionari nel compito
    sum = 0
    for anno in range (first_year, last_year - N):
        sum += diz_medie_annuali [anno]
        media_mobile = sum/N  #questo è sicuramente diverso da come ho fatto ma non mi ircordo come ho fatto al compito
        diz_medie_mobili [anno + N] = media_mobile
    
    diz_finale = {}
    for anno in range (first_year + N, last_year):
        diz_finale [str(anno)] = diz_medie_annuali(anno) - diz_medie_mobili(anno)
    
    return diz_finale

def ControlloTemperatura (inf, sup, first_year, last_year, time_series):
    first_year = int(first_year)
    last_year = int(last_year)
    inf = int(inf)
    sup = int(sup)  #estremi intervallo di temperatura
    lista_anni_abnormali = []
    for elemento in time_series:
        riga = elemento.split(',')
        for media_mensile in riga[1]:
            if media_mensile < inf or media_mensile > sup:  #se una media di un mese è al di fuori dell'intervallo
                lista_anni_abnormali.append(riga[0].split('-'[0])) #aggiungo l'anno di quel m ese ad una lista
    return lista_anni_abnormali



        


        
        

