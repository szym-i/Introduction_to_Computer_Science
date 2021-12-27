#from typing import AsyncContextManager


class NotEnoughPointsError(Exception):
    pass
właściwe_prostokąty = []
def CheckIfDuplicate(posortowane):
    if posortowane not in właściwe_prostokąty:
        właściwe_prostokąty.append(posortowane)
def EnoughPointsCheck(dane):
    if len(dane) < 4:
        raise NotEnoughPointsError
def Look4Rectangle(dane):
    for point1 in dane:
        #print('Sprawdzam teraz---->',point1)
        for point2 in dane:
            #print('Sprawdzam w pionie...')
            if point1[0] == point2[0] and point1 != point2:
                #print(point2)
                #print("Sprawdzam w pioziomie...")
                for point3 in dane:
                    if point1[1] == point3[1] and point1 != point3:
                        #print(point3)
                        for point4 in dane:
                            if point2[1] == point4[1] and point4[0] == point3[0] and point2 != point4:
                                #print(point4)
                                #print('Znalazłem prostokąt o punktach:',point1,point2,point3,point4)
                                prostokąty = [point1,point2,point3,point4]
                                flag = True
                                for point5 in dane:
                                    if point5[1] > min(point1[1],point2[1]) and point5[1] < max(point1[1],point2[1]): #rozbiłem to na dwa ify dla lepszej czytelności
                                        if point5[0] > min(point1[0],point3[0]) and point5[0] < max(point1[0],point3[0]):
                                            flag = False
                                    length1 = abs(point1[1] - point2[1])
                                    length2 = abs(point1[0] - point3[0])
                                if length1 != length2 and flag == True: #sprawdzamy czy prostokąt nie jest kwadratem
                                    posortowane = sorted(prostokąty, key=lambda tup: tup) #sortujemy po krotkach
                                    CheckIfDuplicate(posortowane)
dane = [(1,4),(6,4),(6,1),(1,1),(0,2),(1,5),(8,6),(0,0),(0,1),(1,0),(0,4),(6,0)]

try:
    EnoughPointsCheck(dane)
    Look4Rectangle(dane)
    for prostokąt in właściwe_prostokąty:
        print(prostokąt)
    print('ilośc wykrytych prostokątów',len(właściwe_prostokąty))
except NotEnoughPointsError:
    print('Wprowadziłeś za mało punktów')