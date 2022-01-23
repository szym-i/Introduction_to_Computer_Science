def Max(lista,maks,n)->int: #gdzie n - długość listy(element który będziemy badać) a maks = ostatni element listy
    if n > 0:
        if lista[n-1] > maks: #n-1 bo elementy w liście są indeksowane od 0
            maks = lista[n-1]
        return Max(lista,maks,n-1) #rekurencja
    elif n == 0:
        return maks
def Suma(lista,suma,n)->int: #gdzie n - długość listy
    if n > 0:
        suma += lista[n-1] #dodajemy element n-1 (patrz: 3 linia kodu) z listy
        return Suma(lista,suma,n-1) #rekurencja
    elif n == 0:
        return suma
lista = []
try:
    print('Suma=',Suma(lista,0,len(lista)))
    print('Maksymalny element=',Max(lista,lista[-1],len(lista)))
except TypeError:
    print('Wystąpił jakiś problem z listą')
except IndexError:
    print('Lista jest pusta!')