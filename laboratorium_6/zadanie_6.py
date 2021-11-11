czynniki = []
def rozloz(liczba):
    k = 2
    while liczba != 1:
        while liczba % k == 0:
            liczba //= k
            czynniki.append(k)
        k += 1

    return czynniki
def sprawdz(lista):
    for e in lista:
        if e != 1 and e != 2 and e != 3 and e != 5:
            return "Niewłaściwa liczba"
        else:
            return "Liczba jest dwu-trzy-piątkowa"

n = int(input("Wprowadź swoje N..."))
rozloz(n)
print(sprawdz(czynniki))