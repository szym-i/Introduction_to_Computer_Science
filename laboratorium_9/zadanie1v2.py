import os
macierz= []
def printuj(tablica): #funkcja do printowania macierzy w czytelnej formie
    for lista in tablica:
        print(lista)
def sprawdz(m,n): #sprawdzamy czy wymiary macierz (MxN) są odpowiednie
    if m < 2:
        raise ValueError
    if n < 2:
        raise ValueError
def stworz(macierz,m,n): #tworzymy macierz o podanych wymiarach
    for i in range(m):
        lista = []
        for j in range(n):
            x = int(input(f'''Wprowadz {j+1}. liczbe w {i+1}. wierszu '''))
            lista.append(x)
        macierz.append(lista)
    printuj(macierz)
def dodaj(macierz,m,n):
    for i in range(m):
        for j in range(n):
            x = int(input(f'''Dodaj do {j+1}. liczby w {i+1}. wierszu '''))
            macierz[i][j] += x
    os.system("clear") #czyścimy wyjście przed podaniem wyniku
    print('Wynik dodawania macierzy:')
    printuj(macierz)
def odejmij(macierz,m,n):
    for i in range(m):
        for j in range(n):
            x = int(input(f'''Odejmij od {j+1}. liczby w {i+1}. wierszu '''))
            macierz[i][j] -= x
    os.system("clear")
    print('Wynik odejmowania macierzy:')
    printuj(macierz)
try:
    print('Podaj rozmiary macierzy na których będą wykonywane operacje')
    m = int(input('Ilość wierszy='))
    n = int(input('Ilość kolumn='))
    sprawdz(m,n)
    stworz(macierz,m,n)
    operacja = str(input('Wybierz operację: + lub - >>'))
    if operacja == '+':
        dodaj(macierz,m,n)
    elif operacja == '-':
        odejmij(macierz,m,n)
    else:
        raise KeyError
except ValueError:
    print('Za małe te macierze...')
except KeyError:
    print('Nieobsługiwana operacja')
# PRZYPADKI TESTOWE:
# [11,34]       [2,31]      [13,65]
# [80,86]    +  [0,0]    =  [80,86]
# [21,313]      [311,1]     [332,314]
#
#  [1,71]      [2,1]      [3,72]
#  [96,11]  -  [13,31]  = [109,42]
#  [0,12]      [86,68]    [88,80]