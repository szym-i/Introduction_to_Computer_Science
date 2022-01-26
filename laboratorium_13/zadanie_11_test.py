from laboratorium_13.zadanie_11 import Max
from laboratorium_13.zadanie_11 import Suma
import pytest

#Arrange
list1 = [1,2,3,45,66] 
list2 = [0,0,0,0]
list3 = [31,45,12]
empty = []
#Act
max_list1 = Max(list1,list1[-1],len(list1)) 
max_list2 = Max(list2,list2[-1],len(list2))
max_list3 = Max(list3,list3[-1],len(list3))
suma_list1 = Suma(list1,0,len(list1))
suma_list2 = Suma(list2,0,len(list2))
suma_list3 = Suma(list3,0,len(list3))
suma_empty = Suma(empty,0,len(empty))
#Assert
def test_Max():
    assert max_list1 == 66
    assert max_list2 == 0
    assert max_list3 == 45
    with pytest.raises(IndexError):
        Max(empty,empty[-1],len(empty))
        
def test_Suma():
    assert suma_list1 == 117
    assert suma_list2 == 0
    assert suma_list3 == 88
    assert suma_empty == 0