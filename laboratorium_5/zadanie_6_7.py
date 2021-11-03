a = int(input("Sprawdź czy liczba jest pierwsza: "))  #sprawdź czy liczba jest pierwsza
b = 0
for i in range (1,a+1):
    if a % i == 0:
        b = b+1
        print("Dzielnikiem liczby jest: ",i)
if b <= 2:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")
