#ciąg Fibonacciego - elementy mniejsze od miliona
a = 0
b = 1
c = a + b
print(a)
print(b)
print(c)
while True:
    a = b
    b = c
    c = a + b
    if c < 1000000:
        print(c)