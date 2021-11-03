a = 0 #program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów ciągu Fibonacciego
b = 1
c = a + b
while c < 10000:
    a = b
    b = c
    c = a + b
    iloraz = a / b
    print(a,"/",b,iloraz)