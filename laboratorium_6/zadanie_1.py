print(f'''a^x2+bx+c''')
def delta(a,b,c):
    delta = (b**2) - 4*a*c
    return delta
try:
    a = float(input(f'''Wprowadź a='''))
    b = float(input(f'''Wprowadź b='''))
    c = float(input(f'''Wprowadź c='''))
    d = delta(a,b,c)
    pierwiastek = d**0.5
    if d == 0:
        x0 = -b/(2*a)
        print(f'''Pierwiastek x_0={x0}''')
    else:
        x1=(-b+pierwiastek)/2*a
        x2=(-b-pierwiastek)/2*a
        print(f'''Pierwiastki to x_1={x1} oraz x_2={x2}''')
except:
    print(f'''Delta < 0, brak pierwiastków w zbiorze liczb rzeczywistych''')