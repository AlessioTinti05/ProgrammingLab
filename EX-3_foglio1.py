def palindromo(stringa):
    n = len(stringa)
    for i in range (n // 2):
        if stringa[i] != stringa[n - i - 1]:
            return -1
    return 1

print(palindromo("pollop")) 
    