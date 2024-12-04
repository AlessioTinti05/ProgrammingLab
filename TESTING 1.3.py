import unittest
from ProgrammingLab.fileCSV import CSVfile
from ProgrammingLab.fileCSV import NumericalCSVfile

def test_csvfile():
    csv_file = CSVfile("testingmaybe.csv")
    data = csv_file.get_data()
    print("Dati CSV:", data)
    #?
    Dati_CSV = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    if data not in Dati_CSV:
        raise Exception ("Output non corretto")
    

def test_numerical_csvfile():
    numerical_csv_file = NumericalCSVfile("testingmaybe.csv")
    data = numerical_csv_file.get_data()
    print("Dati numerici CSV:", data)
    #?
    Dati_numerici_CSV = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8, 9.0]]
    if data not in Dati_numerici_CSV:
        raise Exception ("Output non corretto")



if __name__ == "__main__":
    test_csvfile()
    test_numerical_csvfile()

Dati_CSV = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
Dati_numerici_CSV = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8, 9.0]]

#grazie Blackbox