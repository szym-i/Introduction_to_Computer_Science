imie="Szymon"
nazwisko="Milczarczyk"
wiek=19
zwierze="pies"
potrawa="każda"
x=5/7
print("z dokładnością do 1 cyfry", round(x,1))
print("z dokładnością do 3 cyfr", round(x,3))
print("z dokładnością do 5 cyfr", round(x,5))
print("z dokładnością do 10 cyfr", round(x,10))
print(f'''Szymon Milczarczyk, 19, pies, każda potrawa:){round(x,10) }''')
print(imie, nazwisko, wiek, zwierze, potrawa)