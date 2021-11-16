#zauważyłem że gdy j=0, wynik jest zwracany w nieczytelnej postaci (X+0j), stąd funkcja sprawdzenie
def sprawdzenie(x):                   #przykłady:
    if x.imag == 0:                    #1. 1+j * 1-j  -> 2
        if x.real % 1 == 0:            #2. **5        -> 32
            return int(x.real)         #3. +64j       -> 32+64j
        else:                          #4. /8         -> 4+8j
            return x.real   
    else:
        return x
print(f'''KALKULATOR LICZB ZESPOLONYCH \nUWAGA: liczba zespolona ma postać (A+Bj)''')
wynik = complex(input(f'''Wprowadź liczbę zespoloną>>'''))
while True:
    operacja = (input(f'''Wybierz operację: + | - | * | / | ** \n >>'''))
    a = float(input('Wprowadź Re:'))
    b = float(input('Wprowadź Imz:'))
    c = complex(a,b)
    try:
        if operacja == '+':
            wynik += c
            print(wynik)
        elif operacja == '-':
            wynik -= c
            print(wynik)
        elif operacja == '*':
            wynik = wynik * c
            print(wynik)
        elif operacja == '/':
            if c==0:
                raise ZeroDivisionError #zgłaszamy błąd przy dzieleniu przez 0
            else:
                wynik = wynik / c
                print(wynik)
        elif operacja == '**':
            if b == 0:
                wynik = wynik ** a
                print(wynik)
            else:
                raise ValueError #zgłaszamy błąd przy potęgowaniu
        end = input(f'''Czy chcesz wprowadzić nowe dane?T/N''')
        if end == 'N' or end == 'n':
            print(f'''Ostateczny wynik: {sprawdzenie(wynik)}''')
            break
    except ValueError:
        print(f'''Nieobsługiwana operacja''')
    except ZeroDivisionError:
        print(f'''NIE DZIEL PRZEZ 0''')