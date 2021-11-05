lista = [] #Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.
lista_max = []
def nwd(a):
    for i in range(1,a+1):
        if a % i == 0:
            lista.append(i)
    for j in range(1,100):
        if lista.count(j) == 3:
            lista_max.append(j)
if __name__ == "__main__":
    a = int(input("Pierwsza liczba->"))
    b = int(input("Druga liczba---->"))
    c = int(input("Trzecia liczba-->"))
    nwd(a)
    nwd(b)
    nwd(c)
    x = len(lista_max)
    print("NWD(",a,";",b,";",c,") to",lista_max.pop(x-1))