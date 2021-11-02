#ciąg Fibonacciego - elementy mniejsze od miliona
a = 0
b = 1
c = a + b
print(a,"\n",b)
while c < 1000000:
    print(c)
    a = b
    b = c
    c = a + b