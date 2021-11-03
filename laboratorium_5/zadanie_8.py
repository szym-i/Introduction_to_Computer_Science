#Napisać program wyszukujący liczby doskonałe mniejsze od miliona
try:
    n = int(input("Input a positive integer: "))
except:
    print("Your input is not a positive integer!")
    exit()

if (n < 0):
    print("Your input is not a positive integer!")
    exit()