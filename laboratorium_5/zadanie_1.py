a = 0  #ciąg Fibonacciego - elementy mniejsze od miliona
b = 1
c = a + b
print(f'''{a}\n{b}''')
while c < 1000000:
    print(c)
    a = b
    b = c
    c = a + b