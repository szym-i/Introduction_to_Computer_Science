zakres_bin = '01'                    #przypadki testowe:
zakres_oct = '01234567'               #wprowadzamy niepoprawne systemy
zakres_hex = '0123456789ABCDEFabcdef' #wprowadzamy takie same systemy
zakres_dec = '0123456789'             #wprowadzamy niepoprawne liczby (z minusem lub spoza systemu ktory wybralismy)
poprawne_systemy = [2,8,10,16]        #wprowadzamy poprawne liczby (np.)
def sprawdz_systemy(s1,s2):#sprawdzamy czy wybrane systemy są poprawne
    if s1 not in poprawne_systemy:
        raise Exception
    if s2 not in poprawne_systemy:
        raise Exception
    elif s1 == s2:
        print('Co robisz??')
    else:
        operacja_zamiany(s1,s2,liczba)
def sprawdz_liczbe(s1,num1):#sprawdzamy czy wczytana liczba jest w wybranym systemie 
    if s1 == 2:
        for cyfra in num1:
            if cyfra not in zakres_bin:
                raise ValueError
    elif s1 == 8:
        for cyfra in num1:
            if cyfra not in zakres_oct:
                raise ValueError
    elif s1 == 16:
        for cyfra in num1:
            if cyfra not in zakres_hex:
                raise ValueError
    else:
        for cyfra in num1:
            if cyfra not in zakres_dec:
                raise ValueError
def operacja_zamiany(s1,s2,num1):#zamiana ze stringa na dziesietny, i z dziesietnego na docelowy
    sprawdz_liczbe(s1,num1)
    k = liczba_dziesietna = 0 # k - do potęgowania s1
    for cyfra in num1[::-1]:
        if cyfra not in zakres_dec:
            cyfra = cyfra.upper() #zamieniamy małe litery na duże bo ord('a')!=ord('A') 
            cyfra = ord(cyfra)#funkcja odwrotna do chr()-zwraca liczbe pod ktora kryje sie znak np. A
            cyfra -= 55       #pomniejszamy o 55 bo tak wynika z ASCII(A=65,B=66,itd.)
            liczba_dziesietna += cyfra * (s1 ** k)
            k += 1
        elif int(cyfra) < 10:
            liczba_dziesietna += int(cyfra) * (s1 ** k)
            k += 1
    wynik = "" #wynik koncowy
    while liczba_dziesietna > 0:
        reszta = liczba_dziesietna % s2
        if reszta < 10:
            wynik += str(reszta)
            liczba_dziesietna //= s2
        elif reszta >= 10:
            reszta = chr(reszta + 55)#Zwraca napis składający się z jednego znaku,
            wynik += str(reszta)    #którego kod ASCII jest równy liczbie całkowitej
            liczba_dziesietna //= s2
    wynik = wynik[::-1]
    print(f'''Twój wynik to {wynik}''')
try:
    s1 = int(input(f'''Wybierz system początkowy:'''))
    s2 = int(input(f'''Wybierz system docelowy:'''))
    liczba = str(input('Wprowadź swoje naturalne n='))
    sprawdz_systemy(s1,s2)
except ValueError:
    print(f'''Wprowadzona liczba nie jest naturalna/Nie mieści się w wybranym systemie''')
except Exception:
    print(f'''Wybrałeś nieobsługiwany system''')