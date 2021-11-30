lista_pierwsze = [] #pomocnicza lista
lista1 = [] #z liczbami półpierwszymi <N, które są iloczynem dwóch różnych liczb pierwszych
lista2 = [] #z pozostałymi liczbami półpierwszymi <N
def generuj(n): #funkcja przyjmuje liczbe naturalna N
    #szukamy liczb pierwszych do polowy liczby N, poniewaz najwiekszy mozliwy iloczyn mniejszy od N
    #jest rowny i_max = 2 * N/2
    for i in range(2,int(n/2)):
        licznik_dzielnikow = 1
        for j in range(2,int((i**0.5)+1)):  #szukamy dzielnikow do pierwiastka z liczby +1
            if i % j == 0:
                licznik_dzielnikow += 1   #jesli liczba nie jest pierwsza, licznik sie zwiekszy
        if licznik_dzielnikow == 1: 
            lista_pierwsze.append(i)
    for e1 in lista_pierwsze:     #bierzemy kazdy element w liscie liczb pierwszych
        for e2 in lista_pierwsze:   #znowu bierzemy kazdy element z tej samej listy
            if (e2*e1) < n:
                if e2 == e1:
                    lista2.append(e1*e2)
                else:
                    if (e1*e2) not in lista1:  #wpisujemy na lista1 jesli elementu jeszcze tam nie ma
                        lista1.append(e1*e2)
    lista1.sort()  # sortujemy liste aby byla czytelniejsza
    return lista1,lista2
try:
    N = int(input('Wprowadz swoje naturalne N = '))
    N = abs(N) #bierzemy wartosc bezwzgledna, gdyby N bylo ujemne
    print(generuj(N))
except:
    print('Wprowadzona liczba nie jest naturalna')
#przypadki testowe --> najwieksza liczba
# N = 270 --> 267 (3*89)
# N = 5325 --> 5321 (17*313)
# N = 12344 -->  12335 (5*2467)
# N = 150123 -->  150119 (19*7901)
# N = 1000000 --> 999997 (757*1321)