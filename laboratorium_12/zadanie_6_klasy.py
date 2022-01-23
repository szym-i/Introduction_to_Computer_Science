class NotEnoughPointsError(Exception):
    pass

class RectangleDetector:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        for d in data:
            self.data.append(d)

    def calcuate_correct_rectangles(self): #sprawdza czy istnieją 4 punkty tworzące prostokąt (w tym kwadrat)
        self.__ensure_enough_points()
        correct_rectangles = []
        for point1 in self.data:
            for point2 in self.data:
                if point1[0] == point2[0] and point1 != point2:
                    for point3 in dane:
                        if point1[1] == point3[1] and point1 != point3:
                            for point4 in dane:
                                if point2[1] == point4[1] and point4[0] == point3[0]:
                                    rectangle = [point1, point2, point3, point4]
                                    self.__look_for_points_inside_rectangle(point1,point2,point3,rectangle,correct_rectangles)
        return correct_rectangles

    def __append_if_not_square(self, point1, point2, point3, rectangle,correct_rectangles):  # sprawdza czy prostokąt nie jest kwadratem
        a = abs(point1[1] - point2[1])  # długość boków prostokąta
        b = abs(point1[0] - point3[0])
        if a != b:
            self.__append_if_not_duplicate(rectangle, correct_rectangles)

    def __look_for_points_inside_rectangle(self, point1, point2, point3, rectangle, correct_rectangles):#szuka punktów wewnątrz prostokąta
        for point5 in self.data:
            min_y = min(point1[1], point2[1])
            max_y = max(point1[1], point2[1])
            min_x = min(point1[0], point3[0])
            max_x = max(point1[0], point3[0])
            if point5[1] > min_y and point5[1] < max_y and point5[0] > min_x and point5[0] < max_x:
                return
        self.__append_if_not_square(point1, point2, point3, rectangle, correct_rectangles)

    def __append_if_not_duplicate(self, rectangle, correct_rectangles):#sprawdza czy nie wykryto już takiego prostokąta
        sorted_rectangle = sorted(rectangle, key=lambda tup: tup)  # sortujemy po krotkach
        if sorted_rectangle not in correct_rectangles:
            correct_rectangles.append(sorted_rectangle)

    def __ensure_enough_points(self):#sprawdza czy jest wystarczająco punktów aby zbudować prostokąt
        if len(self.data) < 4:
            raise NotEnoughPointsError


def result(correct_rectangles):  #funkcja zwracająca True jeśli istnieje taki prostokąt i False w przeciwnym wypadku
    if len(correct_rectangles) != 0:
        return True
    else:
        return False


dane = [(0,0),(0,1),(0,0)]
#dane = [(0,1),(0,6),(4,1),(4,6),(9,1),(9,6)] #test1 ----> True, 2 prostokąty
#dane = [(0,1),(0,6),(4,1),(4,6),(9,1),(9,6),(1,2)] #test2 ----> False, 0 prostokątów
#dane = [(0, 1), (0, 6), (4, 1), (4, 6), (9, 1), (9, 6), (0, 7), (4, 7), (9, 7)]  # test3 ----> True, 7 prostokątów

try:
    detector = RectangleDetector()
    detector.add_data(dane)
    rectangles = detector.calcuate_correct_rectangles()
    for e in rectangles:
        print(e)
    print('ilośc wykrytych prostokątów', len(rectangles))
    print(result(rectangles))
except NotEnoughPointsError:
    print('Wprowadziłeś za mało punktów')