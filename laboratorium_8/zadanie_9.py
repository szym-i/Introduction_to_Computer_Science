lista_pierwsze = []
lista1 = [] #z liczbami półpierwszymi <N, które są iloczynem dwóch różnych liczb pierwszych
lista2 = [] #z pozostałymi liczbami półpierwszymi <N
def generuj_liczby_pierwsze(n):
    #szukamy liczb pierwszych do polowy liczby N, poniewaz najwiekszy mozliwy iloczyn mniejszy od N
    #jest rowny i_max = 2 * N/2
    for i in range(2,int(n/2)):
        licznik = 1 #licznik dzielnikow liczby
        #szukamy dzielnikow do pierwiastka z liczby
        for j in range(2,int((i**0.5)+1)):
            if i % j == 0:
                licznik += 1 #jesli liczba nie jest pierwsza, licznik sie zwiekszy i program nie wpisze liczby na liste liczb pierwszych
        if licznik == 1: 
            lista_pierwsze.append(i) # liczba pierwsza zostanie wpisana na liste
    for e in lista_pierwsze: #bierzemy kazdy element w liscie liczb pierwszych
        for a in lista_pierwsze: #bierzemy kazdy element z tej samej listy
            if (a*e) < n:  #liczba polpierwsza musi byc < N
                if a == e: #jesli liczba jest iloczynem tych samych liczb wpisujemy na lista2
                    lista2.append(a*e)
                else: #w pozostalych przypadkach
                    if (e*a) not in lista1:#wpisujemy na lista1 jesli elementu jeszcze nie ma na lista1
                        lista1.append(e*a)
    lista1.sort()
    print('Iloczyny dwoch roznych liczb pierwszych(<N):',lista1)
    print('Kwadraty tych samych liczb pierwszych(<N):',lista2)
try:
    n = int(input('Wprowadz swoje naturalne N = '))
    n = abs(n) #gdyby n bylo calkowite ale ujemne, bierzemy wartosc bezwzgledna
    generuj_liczby_pierwsze(n)
except:
    print('Wprowadzona liczba nie jest naturalna')