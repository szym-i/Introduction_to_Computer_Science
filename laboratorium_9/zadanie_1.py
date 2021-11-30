m = int(input('Podaj ilość wierszy '))
n = int(input('Podaj ilość kolumn '))
macierz = []
for i in range(m):
    lista = []
    for j in range(n):
        x = int(input(f'''Wprowadz {j+1} liczbe w {i+1} wierszu'''))
        lista.append(x)
    macierz.append(lista)
print(macierz)