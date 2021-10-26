if __name__ == "__main__":
    s=0
    print("WYBIERZ OPERACJĘ( WPŁATA | WYPŁATA | SPRAWDŹ SALDO )")
    while True:
        print("Co chcesz zrobić w kolejnym kroku? (WPŁATA | WYPŁATA | SPRAWDŹ SALDO | EXIT)")
        operacja = str(input())
        if operacja == "exit" or operacja == "EXIT": break
        elif operacja == "wpłata" or operacja == "WPŁATA":
            print("Podaj PIN")
            pin=int(input(">>"))
            if pin == 1111:
                print("Ile chcesz wpłacić?")
                wplata = int(input(">>"))
                s=s + wplata
                print("STAN KONTA PO WPŁACIE:",s,"$")
            else:
                print("Niepoprawny PIN")
        elif operacja == "wypłata" or operacja == "WYPŁATA":
            print("Podaj PIN")
            pin=int(input(">>"))
            if pin == 1111:
                print("Ile chcesz wypłacić?")
                wyplata = int(input(">>"))
                if wyplata > s:
                    print("BRAK WYSTARCZAJĄCYCH ŚRODKÓW NA KONCIE")
                else:
                    s=s-wyplata
                    print("STAN KONTA PO WYPŁACIE:",s,"$")
            else:
                print("Niepoprawny PIN")
        elif operacja == "sprawdź saldo" or operacja == "SPRAWDŹ SALDO":
            print("Podaj PIN")
            pin=int(input(">>"))
            if pin == 1111:
                print("TWÓJ STAN KONTA WYNOSI:", s, "$")
            else:
                print("Niepoprawny PIN")
        else:
            print("BŁĘDNA OPERACJA, WYBIERZ JEDNĄ SPOŚRÓD: \n | WPŁATA | \n | WYPŁATA |\n | SPRAWDŹ SALDO |")
