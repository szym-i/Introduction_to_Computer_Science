lista = [0,1]
print(f'''Sprawdź czy liczba n jest iloczynem dowolnych elementów ciągu Fibonacciego''')
try:
    n = int(input("Wprowadź n= "))
    a = 0
    b = 1
    c = a + b
    while c <= n:
        lista.append(c)
        a = b
        b = c
        c = a +b
    l = len(lista)
    maks = lista[-1] #bo pierwsza wartość to 0
    if n == maks or n == 0:
        print(f'''Liczba N jest iloczynem {n} oraz 1''')
    else:
        for i in range(l-1,-1,-1):
            h = lista[i]
            if n % h == 0:
                y = n / h
                for j in range(l-1,-1,-1):
                    k = lista[j]
                    if y % k == 0:
                        if h * k == n:
                            print(f'''Liczba {n} jest iloczynem {h} i {k}''')
except:
    print(f'''N nie jest liczbą naturalną''')