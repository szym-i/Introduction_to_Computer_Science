print("Wypisz liczby z przedziału")
a=int(input("OD>"))
b=int(input("DO>"))
if abs(a-b) > 19:
    print("Zawężam przedział do 6 liczb najbliższym średniej(bez średniej)")
    s = (a+b)/2
    if s%1==0:
        print(int(s-3))
        print(int(s-2))
        print(int(s-1))
        print(int(s+1))
        print(int(s+2))
        print(int(s+3))
    else:
        print(int(s-2.5))
        print(int(s-1.5))
        print(int(s-0.5))
        print(int(s+0.5))
        print(int(s+1.5))
        print(int(s+2.5))
else:
    if b < a:
        for i in reversed(range (b,a+1)):
            print(i)
    else:
        while a <= b:
            print(a)
            a += 1