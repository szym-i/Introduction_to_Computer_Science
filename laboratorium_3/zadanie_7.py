print("Wypisz liczby z przedziału")
a=int(input("OD>"))
b=int(input("DO>"))
if abs(a-b) > 19:
    print("Zawężam przedział do 6 liczb najbliższym średniej(bez średniej)")
    s = (a+b)/2
    if s%1==0:
        print(str(s-3)[0:4])
        print(str(s-2)[0:4])
        print(str(s-1)[0:4])
        print(str(s+1)[0:4])
        print(str(s+2)[0:4])
        print(str(s+3)[0:4])
    else:
        print(str(s-2.5)[0:4])
        print(str(s-1.5)[0:4])
        print(str(s-0.5)[0:4])
        print(str(s+0.5)[0:4])
        print(str(s+1.5)[0:4])
        print(str(s+2.5)[0:4])
else:
    if b < a:
        for i in reversed(range (b,a+1)):
            print(i)
    else:
        for i in range (a,b+1):
            print(i)