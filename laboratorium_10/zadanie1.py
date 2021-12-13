import os
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
def print_letters(filename,file):
    try:
        plik = open(filename+'/'+file, "r")
        dict = {}
        for line in plik:
            for e in line:
                if e != '\n' and e != ' ': #odrzucamy znaki nowej linii oraz spacje
                    if e not in dict:
                        dict[e] = 1
                    else:
                        dict[e] += 1
        dict = list(sorted(dict.items(), key=lambda x: x[1], reverse=True))
        print(dict) #pomocnicza linijka
        if len(dict) >= 5:
            print(style.GREEN + f'''Piąty najczęściej występujący znak w pliku {file} to:{dict[4][0]}''')
        else:
            print(style.YELLOW+ f'''Plik {file} ma za mało zmaków''')
    except:
        print(style.MAGENTA + file,'to katalog a nie plik ;)')
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
        print(style.GREEN + 'Zawartość wprowadzonej sciezki:',katalog)
        licznik_zawartosci(katalog,filename)
    except FileNotFoundError:
        print(style.CYAN +'Nie ma takiego katalogu')
    except FileExistsError:
        print(style.RED + 'Brak plików .txt w tym folderze')
while True:
    sciezka = input(style.WHITE + 'Wprowadź lokalizacje pliku: (np./home/szymon/Desktop/test1)')
    read_my_files(sciezka)