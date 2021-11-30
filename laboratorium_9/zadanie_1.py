def sprawdz(m,n):
    if m < 1:
        raise ValueError
    if n < 1:
        raise ValueError
try:
    m = int(input('Podaj ilość wierszy '))
    n = int(input('Podaj ilość kolumn '))
    sprawdz(m,n)
    macierz = []
    for i in range(m):
        lista = []
        for j in range(n):
            x = int(input(f'''Wprowadz {j+1} liczbe w {i+1} wierszu '''))
            lista.append(x)
        macierz.append(lista)
    print(macierz)
except:
    print('Niewłaściwe wymiary macierzy')