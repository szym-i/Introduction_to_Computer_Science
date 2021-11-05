#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
try:
    n = int(input(">>"))
except:
    print("Liczba nie jest naturalna")
a = 0
b = 1
c = a + b
while True:
    multiplication = b*c
    if n > 0:
        if n == multiplication:
            print("Liczba",n,"jest iloczynem dowolnych dwóch kolejnych wyrazów",b,"i",c,"ciągu Fibonacciego ")
            break
        elif n > multiplication:
            a = b
            b = c
            c = a + b
        elif n < multiplication:
            print("Liczba nie jest iloczynem dwóch wyrazów ciągu Fibonacciego")
            break
    if n <= 0: 
        print("Liczba nie jest naturalna")
        break