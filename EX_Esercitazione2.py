class ExamException (Exception):
    pass
class CSVTimeSeriesFile ():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        lista = []
        with open (self.name) as file:
            contenuto = self.name.read()
            for line in contenuto:
                temp_lista = contenuto.split(',')
                for item in temp_lista:
                    lista.append(item)
        
def compute_variations (time_series, first_year, last_year):
    my_diz = {}
    anno = first_year
    sum = 0
    c = 0
    temp_list = []
    while anno <=last_year:  
        for item in time_series:
            if type(item) is str:
                test_num = int(item[0:4])
                if test_num != anno:
                    media = sum/c
                    temp_list.append(media)
                    intervallo = "{}-{}".format(anno, test_num)
                    if len(temp_list) == 2:
                        result = temp_list[1] - temp_list[0]
                        temp_list[0:2] = []
                        my_diz[intervallo] = result
                    anno = test_num
                    c = 0
                    sum = 0
            elif type(item) is int:
                sum += item
                c += 1
    return my_diz

lista1 = ["1949-01", 122, "1949-02", 24, "1950-02", 34, "1950-12", 111]
print (compute_variations (lista1, 1949, 1950))