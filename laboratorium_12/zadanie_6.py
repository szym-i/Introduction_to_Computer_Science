#from typing import AsyncContextManager
class NotEnoughPointsError(Exception):
    pass
właściwe_prostokąty = []
def CheckIfDuplicate(prostokąt):
    posortowany = sorted(prostokąt, key=lambda tup: tup) #sortujemy po krotkach
    if posortowany not in właściwe_prostokąty:
        właściwe_prostokąty.append(posortowany)
def EnoughPointsCheck(dane):
    if len(dane) < 4:
        raise NotEnoughPointsError
def Look4Rectangle(dane):
    for point1 in dane:
        for point2 in dane:
            if point1[0] == point2[0] and point1 != point2:
                for point3 in dane:
                    if point1[1] == point3[1] and point1 != point3:
                        for point4 in dane:
                            if point2[1] == point4[1] and point4[0] == point3[0] and point2 != point4:
                                prostokąt = [point1,point2,point3,point4]
                                flag = True
                                for point5 in dane:
                                    min_y = min(point1[1],point2[1])
                                    max_y = max(point1[1],point2[1])
                                    min_x = min(point1[0],point3[0])
                                    max_x = max(point1[0],point3[0])
                                    if point5[1] > min_y and point5[1] < max_y and point5[0] > min_x and point5[0] < max_x: 
                                        flag = False
                                    length1 = abs(point1[1] - point2[1])
                                    length2 = abs(point1[0] - point3[0])
                                if length1 != length2 and flag == True: #sprawdzamy czy prostokąt nie jest kwadratem
                                    CheckIfDuplicate(prostokąt)
dane = [(1,4),(6,4),(6,1),(1,1),(0,2),(1,5),(8,6),(0,0)]
try:
    EnoughPointsCheck(dane)
    Look4Rectangle(dane)
    for prostokąt in właściwe_prostokąty:
        print(prostokąt)
    print('ilośc wykrytych prostokątów',len(właściwe_prostokąty))
except NotEnoughPointsError:
    print('Wprowadziłeś za mało punktów')