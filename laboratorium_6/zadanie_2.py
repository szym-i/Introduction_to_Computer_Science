#Proszę napisać program wczytujący dwie liczby urojone w postaci algebraicznej, a następnie wykonać następujące operacje arytmetyczne na tych liczbach
print(f'''UWAGA: liczba zespolona ma postać (A+Bj)''')
x1 = complex(input("Wprowadź zespoloną>>"))
x2 = complex(input("Wprowadź drugą liczbę zespoloną>>"))
print(x1,x2)
def suma(c1,c2):
    result = c1 +c2
    if result.imag == 0:  #zauważyłem że gdy część urojona = 0, program zwraca wynik w mniej czytelnej formie (X+0j), ten if jest po to aby zwacał sam X gdy imag = 0
        return result.real
    else:
        return result
def roznica(c1,c2):
    result = c1 - c2
    if result.imag == 0:
        return result.real
    else:
        return result
def mnozenie(c1,c2):
    result = c1 * c2
    if result.imag == 0:
        return result.real
    else:
        return result
def dzielenie(c1,c2):
    if c2 != 0:
        result = c1/c2
        if result.imag == 0:
            return result.real
        else:
            return result
    else:
        return '''NIE DZIEL PRZEZ 0'''
def sprzezenie(c1):
    if c1.imag == 0:
        return '''\nBRAK SPRZĘŻENIA,LICZBA NIE JEST ZESPOLONA'''
    result = c1 -2j*c1.imag
    return result
print(f'''Wynik dodawania:{suma(x1,x2)}\nWynik odejmowania:{roznica(x1,x2)}\nWynik mnożenia:{mnozenie(x1,x2)}\nWynik dzielenia:{dzielenie(x1,x2)}\nSprzężenia tych liczb są równe:{sprzezenie(x1)},{sprzezenie(x2)}''')