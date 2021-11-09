print(f'''Czy liczba jest wielokrotnością dowolnego wyrazu ciągu danego wzorem: A(n)=n∗n+n+1''')
def check_result(x):
    delta = 4 * x - 3
    sqrt = delta ** 0.5
    n1 = (-1 + sqrt)/2
    n2 = (-1 - sqrt)/2
    if n1 % 1 == 0 and n1 > 0:
        print(f'''liczba JEST wielokrotnością dowolnego wyrazu ciągu A(n)=n∗n+n+1 o numerze {int(n1)}''')
    elif n2 % 1 == 0 and n2 > 0:
        print(f'''liczba JEST wielokrotnością dowolnego wyrazu ciągu A(n)=n∗n+n+1 o numerze {int(n2)}''')
    else:
        print(f'''Liczba NIE JEST wielokrotnością dowolonego wyrazu ciągu''')
try:
    b = int(input(f'''Wprowadź liczbę>>'''))
    check_result(b)
except:
    print(f'''Niewłaściwa wartość''')