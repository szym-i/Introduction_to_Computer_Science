a=int(input(">>>"))
b=int(input(">>>"))
if abs(a-b) > 19 :
    print("Zawężam przedział do 6 liczb")
    s = (a+b)/2
    round(s)
    print(s-3)
    print(s-2)
    print(s-1)
    print(s+1)
    print(s+2)
    print(s+3)
else:
    for i in range (a,b+1):
        print(i)
