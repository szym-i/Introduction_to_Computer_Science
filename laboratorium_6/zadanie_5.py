lista = []
lista2 = []
def dec2bin(x):
    while x > 0:
        lista.append(x % 2)
        x //= 2
    if lista == lista[::-1]:
        print(f'''Liczba binarna jest palidromem''')
    else:
        print(f'''Liczba binarna nie jest palidromem''')
def naturalna(x):
    if x < 0:
        print(f'''Liczba jest ujemna''')
        exit()
def palindrom(x,y):
    while x > 0:
        y.append(x % 10)
        x //= 10
    if y == y[::-1]:
        print(f'''Liczba naturalna jest palindromem''')
    else:
        print(f'''Liczba naturalna nie jest palindromem''')
n = int(input(">>"))
naturalna(n)
palindrom(n,lista2)
dec2bin(n)
lista = lista[::-1]
binary = ''
for e in lista:
    binary += str(e)
print(binary)