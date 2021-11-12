print(f'''A/B z dokładnością do N miejsc po kropce dziesiętnej''')
try:
    n = int(input(f'''Wprowadź liczbę naturalną N='''))
    a = int(input(f'''Wprowadź liczbę naturalną A='''))
    b = int(input(f'''Wprowadź liczbę naturalną B='''))
    result = a / b
    print(round(result,n))
except:
    print(f'''Podane zmienne nie są naturalne''')