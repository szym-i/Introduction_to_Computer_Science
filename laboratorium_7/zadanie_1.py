zakres_bin = '01'
zakres_oct = '01234567'
zakres_hex = '0123456789ABCDEFabcdef'
zakres_dec = '0123456789'
poprawne_systemy = [2,8,10,16]
def sprawdz_systemy(s1,s2):#sprawdzamy czy wybrane systemy są poprawne
    if s1 not in poprawne_systemy:
        raise Exception
    if s2 not in poprawne_systemy:
        raise Exception
    elif s1 == s2:
        print('Co robisz gościu??')
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
def operacja_zamiany(s1,s2,num1):#dokończyć to
    sprawdz_liczbe(s1,num1)
    k = num2 = 0 #stała k - do potęgowania s1
    for cyfra in num1[::-1]:
        if cyfra not in zakres_dec:
            cyfra = cyfra.upper() #zamieniamy małe litery na duże bo ord(a)!=ord(A) 
            cyfra = ord(cyfra)    #funkcja odwrotna do chr()
            cyfra -= 55           #pomniejszamy o 55 bo tak wynika z ASCII(A=65,B=66,itd.)
            num2 += cyfra * (s1 ** k)
            k += 1
        elif int(cyfra) < 10:
            num2 += int(cyfra) * (s1 ** k)
            k += 1
    result = ""
    while num2 > 0:
        reszta = num2 % s2
        if reszta < 10:
            result += str(reszta)
            num2 //= s2
        elif num2 % s2 >= 10:
            reszta = chr(reszta + 55)#Zwraca napis składający się z jednego znaku,
            result += str(reszta)    #którego kod ASCII jest równy liczbie całkowitej
            num2 //= s2
    result = result[::-1]
    print(f'''Twój wynik to {result}''')
try:
    s1 = int(input(f'''Wybierz system początkowy:'''))
    s2= int(input(f'''Wybierz system docelowy:'''))
    liczba = str(input('Wprowadź swoje naturalne n='))
    sprawdz_systemy(s1,s2)
except ValueError:
    print(f'''Wprowadzona liczba nie jest naturalna/Nie mieści się w wybranym systemie''')
except Exception:
    print(f'''Wybrałeś nieobsługiwany system''')