lista_pierwsze = []
lista1 = [] #z liczbami półpierwszymi <N, które są iloczynem dwóch różnych liczb pierwszych
lista2 = [] #z pozostałymi liczbami półpierwszymi <N
def generuj(n): #przyjmuje liczbe naturalna N
    #szukamy liczb pierwszych do polowy liczby N, poniewaz najwiekszy mozliwy iloczyn mniejszy od N
    #jest rowny i_max = 2 * N/2
    for i in range(2,int(n/2)):
        licznik = 1 #licznik dzielnikow liczby
        #szukamy dzielnikow do pierwiastka z liczby
        for j in range(2,int((i**0.5)+1)): #UWAGA: gdy nie dodamy 1, program nie bedzie poprawnie dzialal
            if i % j == 0:
                licznik += 1 #jesli liczba nie jest pierwsza, licznik sie zwiekszy i program nie wpisze liczby na liste liczb pierwszych
        if licznik == 1: 
            lista_pierwsze.append(i) # liczba pierwsza zostanie wpisana na liste
    for e1 in lista_pierwsze: #bierzemy kazdy element w liscie liczb pierwszych
        for e2 in lista_pierwsze: #bierzemy kazdy element z tej samej listy
            if (e2*e1) < n:  #liczba polpierwsza musi byc < N
                if e2 == e1: #jesli liczba jest iloczynem tych samych liczb wpisujemy na lista2
                    lista2.append(e1*e2)
                else: #w pozostalych przypadkach
                    if (e1*e2) not in lista1:#wpisujemy na lista1 jesli elementu jeszcze nie ma na lista1
                        lista1.append(e1*e2)
    lista1.sort()
    print('Iloczyny dwoch roznych liczb pierwszych(<N):',lista1)
    print('Iloczyny tych samych liczb pierwszych(<N):',lista2)
    #print('Liczby pierwsze',lista_pierwsze)
try:
    n = int(input('Wprowadz swoje naturalne N = '))
    n = abs(n) #gdyby n bylo calkowite ale ujemne, bierzemy wartosc bezwzgledna
    generuj(n)
except:
    print('Wprowadzona liczba nie jest naturalna')
#przypadki testowe --> najwieksza liczba
# N = 270 --> 267 (3*89)
# N = 5325 --> 5321 (17*313)
# N = 12344 -->  12335 (5*2467)
# N = 150123 -->  150119 (19*7901)
# N = 1000000 --> 999997 (757*1321)