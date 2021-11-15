#Proszę napisać program wczytujący dwie liczby urojone w postaci algebraicznej
print(f'''UWAGA: liczba zespolona ma postać (A+Bj)''')
x1 = complex(input("Wprowadź pierwszą liczbę zespoloną>>"))
x2 = complex(input("Wprowadź drugą liczbę zespoloną>>"))
#zauważyłem że gdy j=0, wynik jest zwracany w nieczytelnej postaci (X+0j), stąd funkcja sprawdzenie
def sprawdzenie(x):  #przykłady: 1. dwie liczby rzeczywiste 2.dwie liczby urojone 3.jedna taka jedna taka 4.
    if x.imag == 0:
        if x.real % 1 == 0:
            return int(x.real)
        else:
            return x.real
    else:
        return x
def suma(c1,c2):
    result = c1 +c2
    return result
def roznica(c1,c2):
    result = c1 - c2
    return result
def mnozenie(c1,c2):
    result = c1 * c2
    return result
def dzielenie(c1,c2):
    if c2 != 0:
        result = c1/c2
        return result
    else:
        return '''NIE DZIEL PRZEZ 0'''
def potegowanie(c1,c2):
    if c1.imag == 0 and c2.imag == 0:
        result = c1.real ** c2.real
        return result
    elif c1.imag == 0:
        result = c2 ** c1.real
        return result
    elif c2.imag == 0:
        result = c1 ** c2.real
        return result
    else:
        return (f'''NIEOBSŁUGIWANA OPERACJA''')
print(f'''1.Wynik dodawania:{sprawdzenie(suma(x1,x2))}
2.Wynik odejmowania:{sprawdzenie(roznica(x1,x2))}
3.Wynik mnożenia:{sprawdzenie(mnozenie(x1,x2))}
4.Wynik dzielenia:{sprawdzenie(dzielenie(x1,x2))}
5.Potęgi tych liczb są równe:{potegowanie(x1,x2)}
6.Sprzężenia tych liczb są równe:{sprawdzenie(x1.conjugate())},{sprawdzenie(x2.conjugate())}''')