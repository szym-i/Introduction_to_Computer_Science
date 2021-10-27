print("KALKULATOR")
wynik = 0
a = float(input("Wprowadź liczbę "))
while True:
    operacja = (input("Wybierz operację:+, -, *, /, **, ^, x."))
    if operacja == "+":
        wynik += a
        print(operacja,wynik)
    elif operacja == "-":
        wynik -= a
        print(operacja,wynik)
    elif operacja == "*":
        print(operacja,wynik)
    elif operacja == "/":
        print(operacja,wynik)
    elif operacja == "**":
        print(operacja,wynik)
    elif operacja == "^":
        print(operacja,wynik)
    elif operacja == "x":
        print(operacja,wynik)