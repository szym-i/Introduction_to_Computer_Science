czynniki = [1]
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
        x = 0
        if e != 1 and e != 2 and e != 3 and e != 5:
            x += 1
    if x == 0:
        return "Liczba jest dwu-trzy-piątkowa"
    else:
        print(f'''Liczba NIE JEST 2,3,5-tkowa''')

n = int(input("Wprowadź swoje N="))
rozloz(n)
print(czynniki)
print(sprawdz(czynniki))