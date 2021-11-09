#Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.
def sumadz(k):
    suma = 0
    for i in range(1,k):
        if k % i == 0:
            suma = suma + i
    return suma
for j in range(1,100000):
    a = sumadz(j)
    if a > j:
        if j == sumadz(a):
            print(f'''Liczby zaprzyjaźnione to {j} i {a}''')