def Max(lista,maks,n): #gdzie n - długość listy a maks = ostatni element listy
    if n > 0:
        if lista[n-1] > maks: #n-1 bo elementy w liście są indeksowane od 0
            maks = lista[n-1]
        Max(lista,maks,n-1) #rekurencja
    elif n == 0:
        print('Maksymalny element w liście to',maks)
def Suma(lista,suma,n): #gdzie n - długość listy
    if n > 0:
        suma += lista[n-1] #dodajemy element n-1 (patrz: 3 linia kodu) z listy
        Suma(lista,suma,n-1) #rekurencja
    elif n == 0:
        print('Suma elementów listy to',suma)
lista = [0,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,0,5,0]
try:
    Suma(lista,0,len(lista))
    Max(lista,lista[-1],len(lista))
except:
    print('Wystąpił jakiś problem z listą')