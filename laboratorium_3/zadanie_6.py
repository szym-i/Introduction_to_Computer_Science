a=int(input("a="))
b=int(input("b="))
#komentarz singleline
'''
komentarz
multiline
'''
if(a < 0 and b < 0):
    print("Liczby są ujemne. Program zakończony!")
elif(a < 0 or b < 0):
    a = abs(a)
    b = abs(b)
    s = a + b
    r = a -b
    m = a*b
    d = a/b
    k = a**2,b**2
    p = a**(1/2), b**(1/2)
    print("Bierzemy wartość bezwzględną z ujemnej liczby i otrzymujemy:")
    print("Suma =",s)
    print("Różnica =",r)
    print("Iloczyn =",m)
    print("Iloraz =",d)
    print("Kwadraty =",k)
    print("Pierwiastki",p)
else:
    s = a + b
    r = a -b
    m = a*b
    d = a/b
    k = a**2,b**2
    p = a**(1/2), b**(1/2)
    print("Otrzymujemy:")
    print("Suma =",s)
    print("Różnica =",r)
    print("Iloczyn =",m)
    print("Iloraz =",d)
    print("Kwadraty =",k)
    print("Pierwiastki =",p)
if(m==10):
    print("Yay!")