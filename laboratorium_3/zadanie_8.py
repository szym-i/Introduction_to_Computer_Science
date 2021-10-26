a = int(input("Podaj wysokość>>"))
for i in range(a):
    if i == 0:
        print(" " * (a-1) + "X")
    else:
        print(" " * (a-i-1) + "*" * (i*2+1))
print(" " * (a-1) + "U")