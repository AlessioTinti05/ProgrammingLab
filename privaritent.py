class ExamException(Exception):
    pass
class CSVTimeSeriesFile:
    def __init__ (self, name):
        self.name = name
        try:
            file = open(self.name, "r")
        except:
            raise ExamException ("Fai schifo file!!11!!1!")
        file.close()

    def get_data(self):
        file = open(self.name, "r")
        data = []
        c = 0
        for line in file:

            elementi = line.strip().split(",")
            lista = []
            if (elementi[0]=="dt"):
                continue

            if c==elementi[0]:
                raise ExamException("Duplicato") #controllo duplicati
            c=elementi[0]
            elementi[1] = int(elementi[1])
            lista.append(elementi[0])
            lista.append(int(elementi[1]))
            data.append(lista)
            #data.append([elementi[0], elementi[1]])
            if elementi[1] <0: #controllo righe
                raise ExamException ("Riga errata")
        file.close()
        return data

time_srs_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')  
time_srs = time_srs_file.get_data()

def compute_variations(time_series, first_year, last_year):
    first_year = int(first_year)
    last_year = int(last_year)

    c=0
    c2=0
    c3=0

    diz_annuale = {}
    for i in time_series:

        linea = i[0].split('-')
        anno = int(linea[0])

        if anno == first_year:
            c +=1
        if anno == last_year:
            c2 += 1

        if anno not in diz_annuale.keys():
            diz_annuale[anno] = []
        diz_annuale[anno].append(int(i[1]))

    if (c==0) or (c2==0): #controllo se primo e ultimo anno presenti in file
        raise ExamException ("Primo/ultimo anno non presenti nel file")

    diz_annuale2 = {}
    for anno in diz_annuale.keys():
        diz_annuale2[anno]=(sum(diz_annuale[anno])/len(diz_annuale[anno]))


    diz_mediemobili = {}
    for anno in range(first_year, last_year+1):
        if anno == last_year:
            continue
        key = str("{}-{}".format(anno, anno+1))
        diz_mediemobili[key] = diz_annuale2[anno+1] - diz_annuale2[anno]
    return diz_mediemobili

z = compute_variations(time_srs, "1901", "1904")
print(z)
