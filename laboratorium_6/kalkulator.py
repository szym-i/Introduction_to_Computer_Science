def sprawdzenie(x):                   #przykłady:
    if x.imag == 0:                    #1. 1+j * 1-j
        if x.real % 1 == 0:            #2. **5
            return int(x.real)         #3. +64j
        else:                          #4. /8
            return x.real
    else:
        return x
print(f'''KALKULATOR LICZB ZESPOLONYCH''')
wynik = complex(input(f'''Wprowadź liczbę zespoloną>>'''))
while True:
    operacja = (input(f'''Wybierz operację: + | - | * | / | **\n >>'''))
    if operacja == "+":
        b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
        wynik += b
        print(wynik)
    elif operacja == "-":
        b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
        wynik -= b
        print(wynik)
    elif operacja == "*":
        b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
        wynik = wynik * b
        print(wynik)
    elif operacja == "/":
        b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
        if b == 0:
            print(f'''NIE DZIEL PRZEZ 0''')
        else:
            wynik = wynik / b
            print(wynik)
    elif operacja == "**":
        b = complex(input(f'''Wprowadź kolejną liczbę zespoloną>>'''))
        if b.imag == 0:
            wynik = wynik ** b
            print(wynik)
        else:
            print(f'''Nieobsługiwana operacja''')
            print(wynik)
    end = input("Czy chcesz wprowadzić nowe dane?T/N")
    if end == "N" or end == "n":
        print(f'''Ostateczny wynik: {sprawdzenie(wynik)}''')
        break