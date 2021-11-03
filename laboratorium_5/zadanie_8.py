print("Wypisz liczby doskonałe < 1000000: ")#Napisać program wyszukujący liczby doskonałe mniejsze od milion
def suma_dzielnikow(j) -> int:
    for j in range (1,10000):
        s = 0
        for i in range (1,j):
            if j % i == 0:
                s = s + i
        if s == j:
            print('Liczba',j,' jest doskonała!')
print(suma_dzielnikow(28))