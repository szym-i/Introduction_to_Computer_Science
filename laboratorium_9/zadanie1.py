import os #biblioteka do czyszczenia wyjscia
macierz1= []
macierz2 =[]
def printuj(tablica): #funkcja do printowania macierzy w czytelnej formie
    for line in tablica:
        print(line)
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
def dodaj(macierz1,macierz2,m,n):
    macierz = [] #tworzymy nową macierz która będzie wynikiem
    for i in range(m):
        lista = []
        for j in range(n):
            lista.append(macierz1[i][j] + macierz2[i][j]) #dodajemy A11 i B11 na listę
        macierz.append(lista)
    print('Wynik dodawania macierzy:')
    printuj(macierz)
def odejmij(macierz1,macierz2,m,n):
    macierz = [] #tworzymy nową macierz która będzie wynikiem
    for i in range(m):
        lista = []
        for j in range(n):
            lista.append(macierz1[i][j] - macierz2[i][j])
        macierz.append(lista)
    print('Wynik odejmowania macierzy:')
    printuj(macierz)
try:
    print('Podaj rozmiary macierzy na których będą wykonywane operacje')
    m = int(input('Ilość wierszy='))
    n = int(input('Ilość kolumn='))
    sprawdz(m,n)
    stworz(macierz1,m,n)
    stworz(macierz2,m,n)
    operacja = str(input('Wybierz operację: + lub - >>'))
    os.system("clear")  #czyścimy wyjście przed podaniem wyniku
    if operacja == '+':
        dodaj(macierz1,macierz2,m,n)
    elif operacja == '-':
        odejmij(macierz1,macierz2,m,n)
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
#  [1,71]      [2,9]      [3,80]
#  [96,11]  -  [13,31]  = [109,42]
#  [0,12]      [86,68]    [88,80]