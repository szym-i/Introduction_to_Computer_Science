def Max(lista,maks,n): #funkcja do znalezienia max elementu
    if n > 0:
        n -= 1 #dekrementujemy n 
        if lista[n-1] > maks:
            maks = lista[n-1]
        Max(lista,maks,n)
    elif n == 0:
        print('Maksymalny element w liście to',maks)
def Suma(lista,suma,n): #funkcja do obliczenia sumy
    if n > 0:
        n -= 1 #dekrementujemy n
        suma += lista[n-1] #wyciągamy ostatni element z listy
        Suma(lista,suma,n)
    elif n == 0:
        print('Suma elementów listy to',suma)
lista = [1,2,3,4]
try:
    Suma(lista,0,len(lista))
    Max(lista,lista[-1],len(lista))
except:
    print('Wystąpił jakiś problem z listą')