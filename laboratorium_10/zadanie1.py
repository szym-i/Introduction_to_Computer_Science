import os
class style(): #do kolorowania outputu
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
class NoTxtFileError(Exception): #własny wyjątek dla braku pliku .txt
    pass
def print_letters(filename,file): #nazwa_folderu,nazwa_pliku
    try:
        opened_file = open(filename+'/'+file, "r") #sklejamy obydwie nazwy tworząc ścieżkę bezwzględną
        dict = {} #słownik do policzenia ilości wystąpień danego znaku
        for line in opened_file:
            for c in line: #(c = character)
                if c != '\n' and c != ' ': #odrzucamy znaki nowej linii oraz spacje
                    if c not in dict:
                        dict[c] = 1
                    else:
                        dict[c] += 1
        dict = list(sorted(dict.items(), key=lambda x: x[1], reverse=True))
        #ze słownika tworzymy listę i sortujemy po drugim elemencie oraz odwracamy ją
        print(dict) #pomocnicza linijka
        if len(dict) >= 5:
            print(style.GREEN + f'''W pliku {file} piątym najczęściej występującym znakiem był:{dict[4][0]}''')
        else:
            print(style.YELLOW+ f'''Plik {file} ma za mało znaków''')
    except: #jeśli folder ma zakończenie .txt to zostanie obsłużony ten wyjątek
        print(style.MAGENTA + file,'to folder a nie plik .txt ;)')
def licznik_zawartosci(files_list,filename):#sprawdzamy czy folder nie jest pusty
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
    #break
#PRZYPADKI TESTOWE SĄ ZALEŻNE OD TWOJEGO ZAGOSPODAROWANIA DYSKU
#Przykładowa ścieżka Linux: /home/user/Desktop/twoj_folder
#Przykładowa ścieżka Windows: C:\Users\Desktop\twoj_folder
#UWAGA: na Windowsie to bez znaczenia czy używamy / czy \