#zauważyłem że gdy j=0, wynik jest zwracany w nieczytelnej postaci (X+0j), stąd funkcja sprawdzenie
def sprawdzenie(x):                   #przykłady:
    if x.imag == 0:                    #1. 1+j * 1-j
        if x.real % 1 == 0:            #2. **5
            return int(x.real)         #3. +64j
        else:                          #4. /8
            return x.real
    else:
        return x
print(f'''KALKULATOR LICZB ZESPOLONYCH \nUWAGA: liczba zespolona ma postać (A+Bj)''')
wynik = complex(input(f'''Wprowadź liczbę zespoloną>>'''))
while True:
    operacja = (input(f'''Wybierz operację: + | - | * | / | ** \n >>'''))
    try:
        if operacja == '+':
            b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
            wynik += b
            print(wynik)
        elif operacja == '-':
            b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
            wynik -= b
            print(wynik)
        elif operacja == '*':
            b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
            wynik = wynik * b
            print(wynik)
        elif operacja == '/':
            b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
            if b == 0:
                raise Exception('Dzielenie przez 0') #zgłaszamy błąd przy dzieleniu przez 0
            else:
                wynik = wynik / b
                print(wynik)
        elif operacja == '**':
            b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
            if b.imag == 0:
                wynik = wynik ** b.real
                print(wynik)
            else:
                raise Exception('Potegowanie') #zgłaszamy błąd przy potęgowaniu
        end = input(f'''Czy chcesz wprowadzić nowe dane?T/N''')
        if end == 'N' or end == 'n':
            print(f'''Ostateczny wynik: {sprawdzenie(wynik)}''')
            break
    except Exception('Potegowanie'):
        print(f'''Nieobsługiwana operacja''')
    except Exception('Dzielenie przez 0'):
        print(f'''NIE DZIEL PRZEZ 0''')