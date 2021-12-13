import os
def print_letters(filename,file):
    try:
        plik = open(filename+'/'+file, "r")
        dict = {}
        for line in plik:
            for e in line:
                if e != '\n':
                    if e not in dict:
                        dict[e] = 1
                    else:
                        dict[e] += 1
        dict = list(sorted(dict.items(), key=lambda x: x[1], reverse=True))
        print('Zawartość',file,':',dict)
        if len(dict) >= 5:
            print('Piąty najczęściej występujący znak to:',dict[4][0])
        else:
            print('Plik ma zbyt mało liter')
    except:
        print(file,'to katalog a nie plik ;)')
def licznik_zawartosci(katalog,filename):
    licznik = 0
    for file in katalog:
        if file.endswith('.txt'):
            licznik += 1
            print_letters(filename,file)
    if licznik == 0:
        raise FileExistsError
def read_my_files(filename):
    try:
        katalog = os.listdir(filename)
        print('Zawartość folderu:',katalog)
        licznik_zawartosci(katalog,filename)
    except FileNotFoundError:
        print('Nie ma takiego katalogu')
    except FileExistsError:
        print('Brak plików .txt w tym folderze')
while True:
    sciezka = input('Wprowadź lokalizacje pliku: (np./home/szymon/Desktop/test1)')
    read_my_files(sciezka)