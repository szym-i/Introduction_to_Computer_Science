def sprawdzenie(x):
    if x < 0:
        print(f'''Liczba X musi być liczbą naturalną''')
    else:
        return x
def rozklad(x):
    min_roznica = x
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            #print(i, int(x/i))
            if min_roznica > abs(x/i-i):
                min_roznica = abs(x/i-i)
                xmax = x/i
                imax = i
    print(x,'=',int(imax),'*',int(xmax))
x = int(input("Wprowadź swój X="))
sprawdzenie(x)
rozklad(x)