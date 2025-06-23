def fattoriale (numero):
    totale = 1
    while (numero):
        totale = totale * numero
        numero = numero - 1
    return totale

print(fattoriale(5))

def fattoriale2 (numero):
    totale = 1
    for i in range(numero , 1, -1):
        totale = totale*i
    return(totale)

print(fattoriale2(5))
