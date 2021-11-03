x = int(input("Wprowadź sumę: ")) #program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie
a = 0
b = 1
c = a + b
suma = a + b + c
while True:
    if x == suma or x == 1 or x == 0:
        print("Istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie",x)
        break
    elif x > suma:
        a = b
        b = c
        c = a + b
        suma = suma + c
    elif x < suma:
        print("Nie istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie",x)
        break