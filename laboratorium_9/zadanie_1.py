def sprawdz(m,n):
    if m < 1:
        raise ValueError
    if n < 1:
        raise ValueError
try:
    print(f'''Podaj rozmiary macierzy na których będą wykonywane operacje''')
    m = int(input('Ilość wierszy='))
    n = int(input('Ilość kolumn='))
    sprawdz(m,n)
    macierz1 = []
    macierz2 = []
    for i in range(m):
        lista = []
        for j in range(n):
            x = int(input(f'''Wprowadz {j+1} liczbe w {i+1} wierszu '''))
            lista.append(x)
        macierz1.append(lista)
    print(macierz1)
    for i in range(m):
        lista = []
        for j in range(n):
            x = int(input(f'''Wprowadz {j+1} liczbe w {i+1} wierszu '''))
            lista.append(x)
        macierz2.append(lista)
    print(macierz2)
    macierz = []
    for k in range(m):
        lista = []
        for h in range(n):
            lista.append(macierz1[k][h] + macierz2[k][h])
        macierz.append(lista)
    print(macierz)
except:
    print('Niewłaściwe wymiary macierzy')