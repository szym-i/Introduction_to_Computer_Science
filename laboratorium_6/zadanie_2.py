#Proszę napisać program wczytujący dwie liczby urojone w postaci algebraicznej, a następnie wykonać następujące operacje arytmetyczne na tych liczbach
print(f'''UWAGA: liczba zespolona ma postać (A+Bj)''')
x1 = complex(input("Wprowadź zespoloną>>"))
x2 = complex(input("Wprowadź drugą liczbę zespoloną>>"))
print(x1,x2)
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
print(f'''Wynik dodawania:{suma(x1,x2)}\nWynik odejmowania:{roznica(x1,x2)}\nWynik mnożenia:{mnozenie(x1,x2)}\nWynik dzielenia:{dzielenie(x1,x2)}''')
 