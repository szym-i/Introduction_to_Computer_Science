print("KALKULATOR")
wynik = float(input("Wprowadź liczbę "))
while True:
    operacja = (input("Wybierz operację:+, -, *, /, **, ^(pierwiastek), x(losowanie): "))
    if operacja == "+":
        b = float(input("Wprowadź kolejną liczbę: "))
        wynik += b
        print(wynik)
    elif operacja == "-":
        b = float(input("Wprowadź kolejną liczbę: "))
        wynik -= b
        print(wynik)
    elif operacja == "*":
        b = float(input("Wprowadź kolejną liczbę: "))
        wynik = wynik * b
        print(operacja,wynik)
    elif operacja == "/":
        b = float(input("Wprowadź kolejną liczbę: "))
        wynik = wynik / b
        print(operacja,wynik)
    elif operacja == "**":
        b = float(input("Wprowadź kolejną liczbę: "))
        wynik = wynik ** b
        print(operacja,wynik)
    elif operacja == "^":
        b = float(input("Podaj stopień pierwiastka: "))
        wynik = wynik ** (1/b)
        print(operacja,wynik)
    elif operacja == "x":
        b = float(input("Końcową liczbę zakresu z którego mam wylosować: "))
        print(operacja,wynik)
    end = input("Czy chcesz wprowadzić nowe dane?T/N")
    if end == "N" or end == "n":
        print("Ostateczny wynik: ", wynik)
        break