def read_my_files(filename):
    plik = open(filename+'.txt', "r")
    print_letters(plik)
def print_letters(plik):
    dict = {}
    for line in plik:
        for e in line:
            if e not in dict:
                dict[e] = 1
            else: 
                dict[e] += 1
    licznik = 0
    print(sorted(dict.values()))
    if len(dict) < 5:
            print('Plik posiada mniej niż 5 znaków')
    else:
        for value in sorted(dict.values()):
            if licznik == 5:
                print(value)
                licznik += 1
            else:
                licznik += 1
while True:
    try:
        filename = str(input('Wprowadź nazwę pliku w tym katalogu lub całą ścieżkę:(bez ."txt")'))
        read_my_files(filename)
        x = input('Czy chcesz wyłączyć program? (N)')
        if x == 'N' or x == 'n':
            break
    except:
        print('Podałeś złą ścieżkę pliku')