macierz1= []
macierz2 =[]
def printuj(tablica): #funkcja do printowania macierzy w czytelnej formie
    for line in tablica:
        print(line)
def sprawdz(m,n):
    if m < 2:
        raise ValueError
    if n < 2:
        raise ValueError
def stworz(macierz,m,n):
    for i in range(m):
        lista = []
        for j in range(n):
            x = int(input(f'''Wprowadz {j+1} liczbe w {i+1} wierszu '''))
            lista.append(x)
        macierz.append(lista)
    printuj(macierz)
def dodaj(macierz1,macierz2,m,n):
    macierz = []
    for i in range(m):
        lista = []
        for j in range(n):
            lista.append(macierz1[i][j] + macierz2[i][j])
        macierz.append(lista)
    print('Wynik dodawania macierzy:')
    printuj(macierz)
def odejmij(macierz1,macierz2,m,n):
    macierz = []
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