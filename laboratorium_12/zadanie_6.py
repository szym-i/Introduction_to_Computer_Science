#from typing import AsyncContextManager
class NotEnoughPointsError(Exception):
    pass
correct_rectangles = []
def CheckIfSquare(point1,point2,point3,rectangle):
    a = abs(point1[1] - point2[1]) #długość boków prostokąta
    b = abs(point1[0] - point3[0])
    if a != b: #sprawdzamy czy prostokąt nie jest kwadratem
        CheckIfDuplicate(rectangle)
def Look4PointsInsideRectangle(point1,point2,point3,rectangle):
    flag = True
    for point5 in dane:
        min_y = min(point1[1],point2[1])
        max_y = max(point1[1],point2[1])
        min_x = min(point1[0],point3[0])
        max_x = max(point1[0],point3[0])
        if point5[1] > min_y and point5[1] < max_y and point5[0] > min_x and point5[0] < max_x:
            flag = False
    if flag == True:
        CheckIfSquare(point1,point2,point3,rectangle)
def CheckIfDuplicate(rectangle):
    sorted_rectangle = sorted(rectangle, key=lambda tup: tup) #sortujemy po krotkach
    if sorted_rectangle not in correct_rectangles:
        correct_rectangles.append(sorted_rectangle)
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
                                rectangle = [point1,point2,point3,point4]
                                Look4PointsInsideRectangle(point1,point2,point3,rectangle)
def Result(): #funkcja zwracająca True jeśli istnieje taki prostokąt i False w przeciwnym wypadku
    if len(correct_rectangles) != 0:
        return True
    else:
        return False
dane = [(0,1),(0,6),(0,6),(4,1),(4,6),(9,1),(9,6),(1,2)] #test2 ----> False, 0 prostokątów
#dane = [(0,1),(0,6),(0,6),(4,1),(4,6),(9,1),(9,6)] #test1 ----> True, 2 prostokąty
try:
    EnoughPointsCheck(dane)
    Look4Rectangle(dane)
    for e in correct_rectangles:
        print(e)
    print('ilośc wykrytych prostokątów',len(correct_rectangles))
    print(Result())
except NotEnoughPointsError:
    print('Wprowadziłeś za mało punktów')