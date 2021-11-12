print(f'''a^x2+bx+c''')
def delta(a,b,c):
    delta = (b**2) - 4*a*c
    return delta
a = float(input(f'''Wprowadź a='''))
b = float(input(f'''Wprowadź b='''))
c = float(input(f'''Wprowadź c='''))
d = delta(a,b,c)
pierwiastek = d**0.5
if d == 0:
    x0 = -b/(2*a)
    print(f'''Pierwiastek x0={x0}''')
elif d >0:
    x1=(-b+pierwiastek)/2*a
    x2=(-b-pierwiastek)/2*a
    print(f'''Pierwiastki to x1={x1} oraz x2={x2}''')
else:
    c1=(-b+pierwiastek)/2*a
    c2=(-b-pierwiastek)/2*a
    print(f'''Rozwiązanie w liczbach urojonych c1={c1} oraz c2={c2}''')



