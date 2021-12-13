import os
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
class NoTxtFileError(Exception):
    pass
def print_letters(filename,file): #sciezka,nazwa_pliku
    try:
        plik = open(filename+'/'+file, "r")
        dict = {}
        for line in plik:
            for c in line:
                if c != '\n' and c != ' ': #odrzucamy znaki nowej linii oraz spacje
                    if c not in dict:
                        dict[c] = 1
                    else:
                        dict[c] += 1
        dict = list(sorted(dict.items(), key=lambda x: x[1], reverse=True)) #sortujemy słownik z policzonymi elementami
        print(dict) #pomocnicza linijka
        if len(dict) >= 5:
            print(style.GREEN + f'''W pliku {file} piątym najczęściej występującym znakiem był:{dict[4][0]}''')
        else:
            print(style.YELLOW+ f'''Plik {file} ma za mało znaków''')
    except:
        print(style.MAGENTA + file,'to folder a nie plik .txt ;)')
def licznik_zawartosci(files_list,filename):
    licznik = 0
    for file in files_list:
        if file.endswith('.txt'):
            licznik += 1
            print_letters(filename,file)
    if licznik == 0:
        raise NoTxtFileError
def read_my_files(filename):
    try:
        files_list = os.listdir(filename) #w ten sposób tworzymy listę z plikami w folderze
        print(style.BLUE + 'Zawartość sciezki:',files_list)
        licznik_zawartosci(files_list,filename)
    except FileNotFoundError:
        print(style.CYAN +'Nie ma takiego katalogu')
    except NoTxtFileError:
        print(style.RED + 'Brak plików .txt w tym folderze')
while True:
    sciezka = input(style.WHITE + 'Wprowadź lokalizacje pliku: (np./home/szymon/Desktop/test1)')
    read_my_files(sciezka)