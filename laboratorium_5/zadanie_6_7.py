a = int(input("Sprawdź czy liczba jest pierwsza: "))  #sprawdź czy liczba jest pierwszaa
b = 0
for i in range (2,a-1):
    if a % i == 0:
        b = b+1
        print("Dzielnikiem liczby jest: ",i)
if b == 0:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")
